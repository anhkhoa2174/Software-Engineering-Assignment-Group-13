<?php

// Kết nối tới database
$dsn = "mysql:host=localhost;dbname=cnpm";
$dbusername = "root";
$dbpassword = "";
$wrongpw = false;

try {
    // Kết nối PDO
    $pdo = new PDO($dsn, $dbusername, $dbpassword);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);  // Set lỗi cho PDO

    // Lấy dữ liệu từ form
    $email = $_POST['email'] ?? ''; // Kiểm tra giá trị đầu vào
    $password = $_POST['password'] ?? '';

    // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }

     // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }
     // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }
     // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }
     // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }
     // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }
     // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }
     // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }
     // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }
     // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }
     // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }
     // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }
     // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }
     // Kiểm tra tính hợp lệ của email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Nếu email không hợp lệ, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=email_invalid");
        exit();
    }

    // Kiểm tra mật khẩu
    if (empty($password)) {
        // Nếu mật khẩu rỗng, chuyển hướng về trang đăng nhập với thông báo lỗi
        header("Location: login_for_spso.html?wrongpw=true&error=password_empty");
        exit();
    }

    // Chuẩn bị câu truy vấn
    $stmt = $pdo->prepare("SELECT * FROM spso WHERE email = :email LIMIT 1");
    $stmt->bindParam(':email', $email);

    // Thực thi câu truy vấn
    $stmt->execute();

    // Kiểm tra kết quả
    if ($stmt->rowCount() > 0) {
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        // Kiểm tra mật khẩu (sử dụng hash để kiểm tra mật khẩu)
        if (password_verify($password, $user['pwd'])) {
            // Nếu mật khẩu chính xác, chuyển hướng tới màn hình chính
            session_start();  // Khởi tạo phiên làm việc
            $_SESSION['user_id'] = $user['id'];  // Lưu thông tin người dùng vào session
            $_SESSION['user_email'] = $user['email'];
            header("Location: homescreen_spso.html?wrongpw=false");
            exit();
        } else {
            // Nếu mật khẩu sai, chuyển hướng về trang đăng nhập với thông báo lỗi
            header("Location: login_for_spso.html?wrongpw=true&error=password_invalid");
            exit();
        }
    } else {
        // Nếu không tìm thấy email trong cơ sở dữ liệu
        header("Location: login_for_spso.html?wrongpw=true&error=email_not_found");
        exit();
    }
} catch (PDOException $e) {
    // Bắt và xử lý lỗi khi kết nối tới cơ sở dữ liệu
    echo "Lỗi kết nối cơ sở dữ liệu: " . $e->getMessage();
    exit();
}

if ($stmt->rowCount() > 0) {
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        // Kiểm tra mật khẩu (sử dụng hash để kiểm tra mật khẩu)
        if (password_verify($password, $user['pwd'])) {
            // Nếu mật khẩu chính xác, chuyển hướng tới màn hình chính
            session_start();  // Khởi tạo phiên làm việc
            $_SESSION['user_id'] = $user['id'];  // Lưu thông tin người dùng vào session
            $_SESSION['user_email'] = $user['email'];
            header("Location: homescreen_spso.html?wrongpw=false");
            exit();
        } else {
            // Nếu mật khẩu sai, chuyển hướng về trang đăng nhập với thông báo lỗi
            header("Location: login_for_spso.html?wrongpw=true&error=password_invalid");
            exit();
        }
    } else {
        // Nếu không tìm thấy email trong cơ sở dữ liệu
        header("Location: login_for_spso.html?wrongpw=true&error=email_not_found");
        exit();
    }
} catch (PDOException $e) {
    // Bắt và xử lý lỗi khi kết nối tới cơ sở dữ liệu
    echo "Lỗi kết nối cơ sở dữ liệu: " . $e->getMessage();
    exit();
}if ($stmt->rowCount() > 0) {
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        // Kiểm tra mật khẩu (sử dụng hash để kiểm tra mật khẩu)
        if (password_verify($password, $user['pwd'])) {
            // Nếu mật khẩu chính xác, chuyển hướng tới màn hình chính
            session_start();  // Khởi tạo phiên làm việc
            $_SESSION['user_id'] = $user['id'];  // Lưu thông tin người dùng vào session
            $_SESSION['user_email'] = $user['email'];
            header("Location: homescreen_spso.html?wrongpw=false");
            exit();
        } else {
            // Nếu mật khẩu sai, chuyển hướng về trang đăng nhập với thông báo lỗi
            header("Location: login_for_spso.html?wrongpw=true&error=password_invalid");
            exit();
        }
    } else {
        // Nếu không tìm thấy email trong cơ sở dữ liệu
        header("Location: login_for_spso.html?wrongpw=true&error=email_not_found");
        exit();
    }
} catch (PDOException $e) {
    // Bắt và xử lý lỗi khi kết nối tới cơ sở dữ liệu
    echo "Lỗi kết nối cơ sở dữ liệu: " . $e->getMessage();
    exit();
}if ($stmt->rowCount() > 0) {
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        // Kiểm tra mật khẩu (sử dụng hash để kiểm tra mật khẩu)
        if (password_verify($password, $user['pwd'])) {
            // Nếu mật khẩu chính xác, chuyển hướng tới màn hình chính
            session_start();  // Khởi tạo phiên làm việc
            $_SESSION['user_id'] = $user['id'];  // Lưu thông tin người dùng vào session
            $_SESSION['user_email'] = $user['email'];
            header("Location: homescreen_spso.html?wrongpw=false");
            exit();
        } else {
            // Nếu mật khẩu sai, chuyển hướng về trang đăng nhập với thông báo lỗi
            header("Location: login_for_spso.html?wrongpw=true&error=password_invalid");
            exit();
        }
    } else {
        // Nếu không tìm thấy email trong cơ sở dữ liệu
        header("Location: login_for_spso.html?wrongpw=true&error=email_not_found");
        exit();
    }
} catch (PDOException $e) {
    // Bắt và xử lý lỗi khi kết nối tới cơ sở dữ liệu
    echo "Lỗi kết nối cơ sở dữ liệu: " . $e->getMessage();
    exit();
}if ($stmt->rowCount() > 0) {
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        // Kiểm tra mật khẩu (sử dụng hash để kiểm tra mật khẩu)
        if (password_verify($password, $user['pwd'])) {
            // Nếu mật khẩu chính xác, chuyển hướng tới màn hình chính
            session_start();  // Khởi tạo phiên làm việc
            $_SESSION['user_id'] = $user['id'];  // Lưu thông tin người dùng vào session
            $_SESSION['user_email'] = $user['email'];
            header("Location: homescreen_spso.html?wrongpw=false");
            exit();
        } else {
            // Nếu mật khẩu sai, chuyển hướng về trang đăng nhập với thông báo lỗi
            header("Location: login_for_spso.html?wrongpw=true&error=password_invalid");
            exit();
        }
    } else {
        // Nếu không tìm thấy email trong cơ sở dữ liệu
        header("Location: login_for_spso.html?wrongpw=true&error=email_not_found");
        exit();
    }
} catch (PDOException $e) {
    // Bắt và xử lý lỗi khi kết nối tới cơ sở dữ liệu
    echo "Lỗi kết nối cơ sở dữ liệu: " . $e->getMessage();
    exit();
}

?>