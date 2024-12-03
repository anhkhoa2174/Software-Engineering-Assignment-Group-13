<?php

// Kết nối tới database
$dsn = "mysql:host=localhost;dbname=cnpm";
$dbusername = "root";
$dbpassword = "";
$wrongpw = false;
try {
    // Kết nối PDO
    $pdo = new PDO("mysql:host=localhost;dbname=cnpm", "root", "");

    // Lấy dữ liệu từ form
    $email = $_POST['email'] ?? ''; // Kiểm tra giá trị đầu vào
    $password = $_POST['password'] ?? '';

    // Chuẩn bị câu truy vấn
    $stmt = $pdo->prepare("SELECT * FROM users WHERE email = :email AND pwd = :password");
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':password', $password);

    // Thực thi câu truy vấn
    $stmt->execute();

    // Kiểm tra kết quả
    if ($stmt->rowCount() > 0) {
        header("Location: index.html?wrongpw=false");
        exit();
    } else {
        header("Location: login_for_student.html?wrongpw=true");
        exit();
    }
} catch (PDOException $e) {
    echo "Lỗi: " . $e->getMessage();
}