import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Account {
    private int accountId;
    private String accountType;
    private double balance;

    public Account(int accountId, String accountType, double balance) {
        this.accountId = accountId;
        this.accountType = accountType;
        this.balance = balance;
    }

    public int getAccountId() {
        return accountId;
    }

    public String getAccountType() {
        return accountType;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
        } else {
            System.out.println("Insufficient funds!");
        }
    }

    public void transfer(Account recipient, double amount) {
        if (amount <= balance) {
            balance -= amount;
            recipient.deposit(amount);
        } else {
            System.out.println("Insufficient funds!");
        }
    }
}

class User {
    private int userId;
    private String username;
    private String password;
    private List<Account> accounts;

    public User(int userId, String username, String password) {
        this.userId = userId;
        this.username = username;
        this.password = password;
        this.accounts = new ArrayList<>();
    }

    public int getUserId() {
        return userId;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public List<Account> getAccounts() {
        return accounts;
    }

    public void addAccount(Account account) {
        accounts.add(account);
    }
}

class BankingSystem {
    private Connection connection;

    public BankingSystem() {
        // Initialize database connection (SQLite in-memory for simplicity)
        try {
            Class.forName("org.sqlite.JDBC");
            connection = DriverManager.getConnection("jdbc:sqlite::memory:");
            initializeDatabase();
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }

    private void initializeDatabase() throws SQLException {
        Statement statement = connection.createStatement();
        statement.execute("CREATE TABLE IF NOT EXISTS users (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "username TEXT NOT NULL," +
                "password TEXT NOT NULL)");

        statement.execute("CREATE TABLE IF NOT EXISTS accounts (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "user_id INTEGER," +
                "account_type TEXT NOT NULL," +
                "balance REAL DEFAULT 0," +
                "FOREIGN KEY (user_id) REFERENCES users(id))");
    }

    public User registerUser(String username, String password) {
        try {
            PreparedStatement statement = connection.prepareStatement(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    Statement.RETURN_GENERATED_KEYS);
            statement.setString(1, username);
            statement.setString(2, password);
            statement.executeUpdate();

            ResultSet generatedKeys = statement.getGeneratedKeys();
            if (generatedKeys.next()) {
                int userId = generatedKeys.getInt(1);
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Account {
    private int accountId;
    private String accountType;
    private double balance;

    public Account(int accountId, String accountType, double balance) {
        this.accountId = accountId;
        this.accountType = accountType;
        this.balance = balance;
    }

    public int getAccountId() {
        return accountId;
    }

    public String getAccountType() {
        return accountType;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
        } else {
            System.out.println("Insufficient funds!");
        }
    }

    public void transfer(Account recipient, double amount) {
        if (amount <= balance) {
            balance -= amount;
            recipient.deposit(amount);
        } else {
            System.out.println("Insufficient funds!");
        }
    }
}

class User {
    private int userId;
    private String username;
    private String password;
    private List<Account> accounts;

    public User(int userId, String username, String password) {
        this.userId = userId;
        this.username = username;
        this.password = password;
        this.accounts = new ArrayList<>();
    }

    public int getUserId() {
        return userId;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public List<Account> getAccounts() {
        return accounts;
    }

    public void addAccount(Account account) {
        accounts.add(account);
    }
}

class BankingSystem {
    private Connection connection;

    public BankingSystem() {
        // Initialize database connection (SQLite in-memory for simplicity)
        try {
            Class.forName("org.sqlite.JDBC");
            connection = DriverManager.getConnection("jdbc:sqlite::memory:");
            initializeDatabase();
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }

    private void initializeDatabase() throws SQLException {
        Statement statement = connection.createStatement();
        statement.execute("CREATE TABLE IF NOT EXISTS users (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "username TEXT NOT NULL," +
                "password TEXT NOT NULL)");

        statement.execute("CREATE TABLE IF NOT EXISTS accounts (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "user_id INTEGER," +
                "account_type TEXT NOT NULL," +
                "balance REAL DEFAULT 0," +
                "FOREIGN KEY (user_id) REFERENCES users(id))");
    }

    public User registerUser(String username, String password) {
        try {
            PreparedStatement statement = connection.prepareStatement(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    Statement.RETURN_GENERATED_KEYS);
            statement.setString(1, username);
            statement.setString(2, password);
            statement.executeUpdate();

            ResultSet generatedKeys = statement.getGeneratedKeys();
            if (generatedKeys.next()) {
                int userId = generatedKeys.getInt(1);
                return new User(userId, username, password);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public User loginUser(String username, String password) {
        try {
            PreparedStatement statement = connection.prepareStatement(
                    "SELECT * FROM users WHERE username = ? AND password = ?");
            statement.setString(1, username);
            statement.setString(2, password);

            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                int userId = resultSet.getInt("id");
                return new User(userId, username, password);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public void createAccount(User user, String accountType) {
        try {
            PreparedStatement statement = connection.prepareStatement(
                    "INSERT INTO accounts (user_id, account_type) VALUES (?, ?)",
                    Statement.RETURN_GENERATED_KEYS);
            statement.setInt(1, user.getUserId());
            statement.setString(2, accountType);
            statement.executeUpdate();

            ResultSet generatedKeys = statement.getGeneratedKeys();
            if (generatedKeys.next()) {
                int accountId = generatedKeys.getInt(1);
                Account account = new Account(accountId, accountType, 0);
                user.addAccount(account);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        BankingSystem bankingSystem = new BankingSystem();

        // User Registration
        User user1 = bankingSystem.registerUser("user1", "password123");
        System.out.println("User Registration Successful!");

        // User Login
        User loggedInUser = bankingSystem.loginUser("user1", "password123");
        if (loggedInUser != null) {
            System.out.println("Login Successful!");

            // Create Accounts
            bankingSystem.createAccount(loggedInUser, "Savings");
            bankingSystem.createAccount(loggedInUser, "Checking");

            // Perform Transactions
            Account savingsAccount = loggedInUser.getAccounts().get(0);
            Account checkingAccount = loggedInUser.getAccounts().get(1);

            savingsAccount.deposit(1000);
            checkingAccount.withdraw(200);
            savingsAccount.transfer(checkingAccount, 300);

            // Display Balances
            System.out.println("Savings Account Balance: $" + savingsAccount.getBalance());
            System.out.println("Checking Account Balance: $" + checkingAccount.getBalance());
        } else {
            System.out.println("Invalid credentials.");
        }
    }
}
￼Enter                return new User(userId, username, password);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public User loginUser(String username, String password) {
        try {
            PreparedStatement statement = connection.prepareStatement(
                    "SELECT * FROM users WHERE username = ? AND password = ?");
            statement.setString(1, username);
            statement.setString(2, password);

            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                int userId = resultSet.getInt("id");
                return new User(userId, username, password);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

blic void createAccount(User user, String accountType) {
        try {
            PreparedStatement statement = connection.prepareStatement(
                    "INSERT INTO accounts (user_id, account_type) VALUES (?, ?)",
                    Statement.RETURN_GENERATED_KEYS);
            statement.setInt(1, user.getUserId());
            statement.setString(2, accountType);
            statement.executeUpdate();

            ResultSet generatedKeys = statement.getGeneratedKeys();
            if (generatedKeys.next()) {
                int accountId = generatedKeys.getInt(1);
                Account account = new Account(accountId, accountType, 0);
                user.addAccount(account);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        BankingSystem bankingSystem = new BankingSystem();

        // User Registration
        User user1 = bankingSystem.registerUser("user1", "password123");
        System.out.println("User Registration Successful!");
