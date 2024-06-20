# Muhammad Faizan Akram (FA23-BBD-090)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#

# Imports
import streamlit as st
from account_management import Account, Transaction
from reporting import Reporting
import matplotlib.pyplot as plt


#---------------------------------------------------------------------------------------------#
# Dummy data
accounts = [Account(1, "Cash", "Asset", 1000), Account(2, "Bank", "Asset", 5000)]
transactions = [Transaction(1, "2024-01-01", 500, "Debit", accounts[0]), Transaction(2, "2024-01-02", 1000, "Credit", accounts[1])]


#---------------------------------------------------------------------------------------------#
# Reporting Object
reporting = Reporting(accounts, transactions)


#---------------------------------------------------------------------------------------------#
# User authentication (simple username/password for demo)
def login(username, password):
    if username == "admin" and password == "password":
        return True
    else:
        return False


#---------------------------------------------------------------------------------------------#
# Chatbot to answer queries about accounts and transactions
def chatbot(query):
    query = query.lower()
    if "total assets" in query:
        total_assets = sum(account.get_balance() for account in accounts if account.get_account_type() == "Asset")
        return f"Total Assets: {total_assets}"
    elif "total liabilities" in query:
        total_liabilities = sum(account.get_balance() for account in accounts if account.get_account_type() == "Liability")
        return f"Total Liabilities: {total_liabilities}"
    elif "equity" in query:
        total_assets = sum(account.get_balance() for account in accounts if account.get_account_type() == "Asset")
        total_liabilities = sum(account.get_balance() for account in accounts if account.get_account_type() == "Liability")
        equity = total_assets - total_liabilities
        return f"Equity: {equity}"
    elif "account balance" in query:
        account_id = int(query.split()[-1])
        account = next((acc for acc in accounts if acc.get_account_id() == account_id), None)
        if account:
            return f"Account ID: {account.get_account_id()}, Balance: {account.get_balance()}"
        else:
            return "Account not found."
    else:
        return "I didn't understand that. Please ask about 'total assets', 'total liabilities', 'equity', or 'account balance <account_id>'."


#---------------------------------------------------------------------------------------------#
# Streamlit Interface
st.title("Accounting Management System")
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login(username, password):
            st.session_state.logged_in = True
        else:
            st.error("Incorrect username or password")


#---------------------------------------------------------------------------------------------#
# Sidebar and Chatbot Interface
if st.session_state.logged_in:
    st.sidebar.title("Menu")
    option = st.sidebar.selectbox("Select an option", ["Manage Accounts", "Record Transactions", "Generate Reports"])

    st.sidebar.subheader("Chatbot")
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    query = st.sidebar.text_input("Ask me anything about your accounts and transactions:")
    if st.sidebar.button("Submit"):
        response = chatbot(query)
        st.session_state.chat_history.append(f"You: {query}")
        st.session_state.chat_history.append(f"Bot: {response}")

    st.sidebar.write("\n".join(st.session_state.chat_history))


#---------------------------------------------------------------------------------------------#
# Account Management
    if option == "Manage Accounts":
        st.subheader("Manage Accounts")
        account_id = st.number_input("Account ID", min_value=1, step=1)
        account_name = st.text_input("Account Name")
        account_type = st.selectbox("Account Type", ["Asset", "Liability", "Equity"])
        balance = st.number_input("Balance", min_value=0, step=1)
        
        if st.button("Add Account"):
            new_account = Account(account_id, account_name, account_type, balance)
            accounts.append(new_account)
            st.success(f"Account {account_name} added successfully!")

        st.write("Current Accounts:")
        for account in accounts:
            st.write(f"ID: {account.get_account_id()}, Name: {account.get_account_name()}, Type: {account.get_account_type()}, Balance: {account.get_balance()}")


#---------------------------------------------------------------------------------------------#
# Transaction Recording
    elif option == "Record Transactions":
        st.subheader("Record Transactions")
        transaction_id = st.number_input("Transaction ID", min_value=1, step=1)
        date = st.date_input("Date")
        amount = st.number_input("Amount", min_value=0.0, step=0.01)
        transaction_type = st.selectbox("Transaction Type", ["Debit", "Credit"])
        account_id = st.selectbox("Account", [account.get_account_id() for account in accounts])

        if st.button("Record Transaction"):
            account = next(acc for acc in accounts if acc.get_account_id() == account_id)
            new_transaction = Transaction(transaction_id, date, amount, transaction_type, account)
            transactions.append(new_transaction)
            if transaction_type == "Debit":
                account.set_balance(account.get_balance() - amount)
            else:
                account.set_balance(account.get_balance() + amount)
            st.success(f"Transaction recorded successfully!")

        st.write("Current Transactions:")
        for transaction in transactions:
            st.write(f"ID: {transaction.get_transaction_id()}, Date: {transaction.get_date()}, Amount: {transaction.get_amount()}, Type: {transaction.get_transaction_type()}, Account: {transaction.get_account().get_account_name()}")


#---------------------------------------------------------------------------------------------#
# Report Generation
    elif option == "Generate Reports":
        st.subheader("Generate Reports")
        report_type = st.selectbox("Report Type", ["Account Balance Report", "Transaction History", "Financial Summary"])
        
        if report_type == "Account Balance Report":
            st.write("Account Balance Report")
            for account in accounts:
                st.write(f"ID: {account.get_account_id()}, Name: {account.get_account_name()}, Balance: {account.get_balance()}")

            # Graph for Account Balances
            account_names = [account.get_account_name() for account in accounts]
            balances = [account.get_balance() for account in accounts]
            plt.bar(account_names, balances)
            plt.xlabel('Account Name')
            plt.ylabel('Balance')
            plt.title('Account Balances')
            st.pyplot(plt)

        elif report_type == "Transaction History":
            account_id = st.selectbox("Select Account", [account.get_account_id() for account in accounts])
            st.write(f"Transaction History for Account ID {account_id}")
            for transaction in transactions:
                if transaction.get_account().get_account_id() == account_id:
                    st.write(f"ID: {transaction.get_transaction_id()}, Date: {transaction.get_date()}, Amount: {transaction.get_amount()}, Type: {transaction.get_transaction_type()}")

        elif report_type == "Financial Summary":
            st.write("Financial Summary Report")
            total_assets = sum(account.get_balance() for account in accounts if account.get_account_type() == "Asset")
            total_liabilities = sum(account.get_balance() for account in accounts if account.get_account_type() == "Liability")
            equity = total_assets - total_liabilities
            st.write(f"Total Assets: {total_assets}")
            st.write(f"Total Liabilities: {total_liabilities}")
            st.write(f"Equity: {equity}")

            # Graph for Financial Summary
            labels = 'Assets', 'Liabilities', 'Equity'
            sizes = [total_assets, total_liabilities, equity]
            colors = ['gold', 'lightcoral', 'lightskyblue']
            explode = (0.1, 0, 0)
            plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
            plt.axis('equal')
            plt.title('Financial Summary')
            st.pyplot(plt)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#