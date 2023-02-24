<?php
$host = 'bankdb'; // or IP address of the MySQL server
$username = 'user';
$password = 'my-secure-pw';
$database = 'bankdb';

// Connect to the MySQL server
$conn = mysqli_connect($host, $username, $password, $database);

// Check for errors
if (!$conn) {
    die('Connection failed: ' . mysqli_connect_error());
}

function filter($str) {
    $str = strtolower($str);
    $str = str_replace("select", '', $str);
    return $str;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get the username and password from the login form
    $username = $_POST['username'];
    $password = $_POST['password'];

    $username = filter($username);
    $password = filter($password);

    // Hash the password with SHA-256
    $hash = $password;

    // Construct the SQL query
    $sql = "SELECT * FROM users WHERE username='$username' AND password='$hash';";

    // Execute the query
    $result = mysqli_query($conn, $sql);
    $str = '';
    if (!$result) {
        //die('Query failed: ' . mysqli_error($conn));
    } else {
        $rows = mysqli_fetch_all($result, MYSQLI_ASSOC);

        // Convert the array to a string
        $str = implode("\n", array_map(function($row) {
            return implode("\t", $row);
        }, $rows));
    }

    // Check if the query returned any rows
    if (mysqli_num_rows($result) > 0) {
        // Login successful
        $_SESSION['username'] = $username;
        $error = '';
    } else {
        // Login failed
        $error = 'Invalid username or password';
    }
}

?>

<!DOCTYPE html>
<html>
<head>
    <title>Login - Bank Database CTF</title>
</head>
<body>
    <h1>Login - Bank Database CTF</h1>
    <span>Try looking in the flags table. Columns: flag, value</span>
    <form method="post">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required><br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required><br>
        <input type="submit" value="Login">
    </form>
    <?php if (isset($sql)): ?>
        <p><?php echo $sql; ?></p>
    <?php endif; ?>
    <?php if (isset($str)): ?>
        <h2>Query Results</h2>
        <p style="white-space: pre-wrap;"><?php echo $str; ?></p>
    <?php endif; ?>
</body>
</html>
