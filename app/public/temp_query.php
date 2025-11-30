<?php
define('DB_NAME', 'local');
define('DB_USER', 'root');
define('DB_PASSWORD', 'root');
define('DB_HOST', 'localhost');

$conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}

$result = $conn->query("SELECT meta_value FROM wp_postmeta WHERE post_id = 21 AND meta_key = '_elementor_data' LIMIT 1");
if ($row = $result->fetch_assoc()) {
    echo $row['meta_value'];
}
$conn->close();
?>