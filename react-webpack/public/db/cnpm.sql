-- Bảng User
CREATE TABLE "User" (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(100),
    profile_picture VARCHAR(255),
    id SERIAL UNIQUE
);

-- Bảng Student (kế thừa từ User)
CREATE TABLE "Student" (
    username VARCHAR(50) PRIMARY KEY REFERENCES "User"(username),
    account_balance NUMERIC(10, 2) DEFAULT 0
);

-- Bảng SPSO (kế thừa từ User)
CREATE TABLE "SPSO" (
    username VARCHAR(50) PRIMARY KEY REFERENCES "User"(username)
);

-- Bảng Printer
CREATE TABLE "Printer" (
    printer_id SERIAL PRIMARY KEY,
    status VARCHAR(50),
    slot INT,
    branch VARCHAR(100),
    building VARCHAR(100),
    room VARCHAR(50)
);

-- Bảng quản lý mối quan hệ giữa SPSO và Printer
CREATE TABLE "Manages" (
    username VARCHAR(50) REFERENCES "SPSO"(username),
    printer_id INT REFERENCES "Printer"(printer_id),
    PRIMARY KEY (username, printer_id)
);

-- Bảng Transaction
CREATE TABLE "Transaction" (
    trans_id SERIAL PRIMARY KEY,
    price NUMERIC(10, 2) NOT NULL,
    no_pages INT NOT NULL,
    status VARCHAR(50),
    student_username VARCHAR(50) REFERENCES "Student"(username)
);

-- Bảng Notification
CREATE TABLE "Notification" (
    noti_id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    username VARCHAR(50) REFERENCES "User"(username)
);

-- Bảng Uses (mối quan hệ giữa User và Printer)
CREATE TABLE "Uses" (
    printer_id INT REFERENCES "Printer"(printer_id),
    username VARCHAR(50) REFERENCES "User"(username),
    file_type VARCHAR(50),
    file_name VARCHAR(255),
    file_size NUMERIC(10, 2),
    no_pages INT,
    status VARCHAR(50),
	time TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (printer_id, username, file_name)
);

-- Insert vào bảng User
INSERT INTO "User" (username, password, name, profile_picture) 
VALUES
('khoa', 'password123', 'Khoa', 'profile_khoa.jpg'),
('duc_huy', 'password456', 'Đức Huy', 'profile_duc_huy.jpg'),
('tien_dat', 'password789', 'Tiến Đạt', 'profile_tien_dat.jpg');

-- Insert vào bảng Student (kế thừa từ bảng User)
INSERT INTO "Student" (username, account_balance) 
VALUES
('khoa', 100),
('tien_dat', 100);

-- Insert vào bảng SPSO (kế thừa từ bảng User)
INSERT INTO "SPSO" (username) 
VALUES ('duc_huy');  -- Giả sử Đức Huy là SPSO

-- Insert vào bảng Printer
INSERT INTO "Printer" (status, slot, branch, building, room) 
VALUES
('Sẵn sàng', 3, 'CS1', 'Tòa B1', 'Phòng 101'),
('Sẵn sàng', 3, 'CS2', 'Tòa H1', 'Phòng 202'),
('Sẵn sàng', 3, 'CS1', 'Tòa B2', 'Phòng 303');

INSERT INTO "Printer" (printer_id, status, slot, branch, building, room) 
VALUES
('2','Sẵn sàng', 3, 'CS1', 'Tòa B1', 'Phòng 101'),
('4','Sẵn sàng', 3, 'CS1', 'Tòa B1', 'Phòng 101'),
('5','Sẵn sàng', 3, 'CS1', 'Tòa B1', 'Phòng 101'),
('6','Sẵn sàng', 3, 'CS1', 'Tòa B1', 'Phòng 101'),
('7','Sẵn sàng', 3, 'CS1', 'Tòa B1', 'Phòng 101'),
('8','Sẵn sàng', 3, 'CS1', 'Tòa B1', 'Phòng 101'),
('9','Sẵn sàng', 3, 'CS1', 'Tòa B1', 'Phòng 101');

update "Printer"
set room = 'Phòng 303'
where printer_id = '3'

select * from "Transaction"

-- Insert vào bảng Manages (quản lý mối quan hệ giữa SPSO và Printer)
INSERT INTO "Manages" (username, printer_id) 
VALUES
('duc_huy', 1),('duc_huy', 2),
('duc_huy', 3),('duc_huy', 4),('duc_huy', 5),('duc_huy', 6),('duc_huy', 7),('duc_huy', 8),('duc_huy', 9);

-- Insert vào bảng Transaction
INSERT INTO "Transaction" (price, no_pages, status, student_username) 
VALUES
(5000, 5, 'Đã thanh toán', 'khoa'),
(2000, 2, 'Lỗi Thanh Toán', 'tien_dat');

-- Insert vào bảng Notification
INSERT INTO "Notification" (content, username) 
VALUES
('In thành công!', 'khoa'),
('In thành công!', 'tien_dat');
INSERT INTO "Notification" (content, username) 
VALUES
('In thất bại!', 'khoa');
INSERT INTO "Notification" (content, username) 
VALUES
('In thành công!', 'khoa');
INSERT INTO "Notification" (content, username) 
VALUES
('In thất bại!', 'khoa')

-- Insert vào bảng Uses (mối quan hệ giữa User và Printer)
INSERT INTO "Uses" (printer_id, username, file_type, file_name, file_size, no_pages, status) 
VALUES
(1, 'khoa', 'PDF', 'document1.pdf', 1.5, 5, 'Hoàn thành'),
(3, 'tien_dat', 'DOCX', 'assignment.docx', 0.5, 2, 'Lỗi in');


INSERT INTO "Uses" (printer_id, username, file_type, file_name, file_size, no_pages, status) 

VALUES

(1, 'khoa', 'DOCX', 'btlmmt.docx', 0.5, 2, 'Lỗi in');



ALTER TABLE "Transaction"

ADD COLUMN "date" DATE DEFAULT CURRENT_DATE;



ALTER TABLE "Transaction" ALTER COLUMN "price" SET DATA TYPE NUMERIC(10, 0);



INSERT INTO "Transaction" (price, no_pages, status, student_username) 

VALUES

(5000, 5, 'Đã thanh toán', 'khoa'),

(2000, 2, 'Lỗi thanh toán', 'tien_dat'),

(51000, 51, 'Đã thanh toán', 'tien_dat'),

(23000, 23, 'Đã thanh toán', 'tien_dat'),

(100000, 100, 'Lỗi thanh toán', 'tien_dat'),

(5000, 5, 'Đã thanh toán', 'tien_dat'),

(5000, 5, 'Đã thanh toán', 'tien_dat'),

(4000, 4, 'Đã thanh toán', 'tien_dat'),

(13000, 13, 'Đã thanh toán', 'tien_dat');



ALTER TABLE "Uses"

ADD COLUMN paper_orientation VARCHAR(10) CHECK (paper_orientation IN ('Ngang', 'Dọc')),

ADD COLUMN print_sides VARCHAR(10) CHECK (print_sides IN ('1 mặt', '2 mặt')),

ADD COLUMN num_copies INT DEFAULT 1;



UPDATE "Uses"

SET paper_orientation = 'Dọc'



UPDATE "Uses"

SET print_sides = '1 mặt'

ALTER TABLE "User"
    ALTER COLUMN profile_picture TYPE BYTEA
    USING profile_picture::bytea;

UPDATE "User"
SET profile_picture = pg_read_binary_file('D:\duchuy.png')
WHERE username = 'duc_huy';
--mỗi máy nhớ đổi đường dẫn để thêm ảnh vào user

UPDATE "User"
SET profile_picture = pg_read_binary_file('D:\BTL_SE\Software-Engineering-Assignment-Group-13\react-webpack\public\backend\static\images\anhkhoa.png')
WHERE username = 'khoa';
--mỗi máy nhớ đổi đường dẫn để thêm ảnh vào user

UPDATE "User"
SET profile_picture = pg_read_binary_file('D:\BTL_SE\Software-Engineering-Assignment-Group-13\react-webpack\public\backend\static\images\dat.png')
WHERE username = 'tien_dat';
--mỗi máy nhớ đổi đường dẫn để thêm ảnh vào user

CREATE OR REPLACE VIEW SPSO_PRINTINGHISTORY AS

SELECT "User".NAME, PRINTER_ID, FILE_TYPE, FILE_NAME, FILE_SIZE, NO_PAGES, STATUS, TIME, paper_orientation, print_sides, num_copies

FROM "User" JOIN "Uses" ON "User".USERNAME = "Uses".USERNAME



CREATE OR REPLACE VIEW SPSO_PRINTINGHISTORY AS

SELECT "User".NAME, PRINTER_ID, FILE_TYPE, FILE_NAME, FILE_SIZE, NO_PAGES, STATUS, TIME, paper_orientation, print_sides, num_copies

FROM "User" JOIN "Uses" ON "User".USERNAME = "Uses".USERNAME



DROP VIEW spso_printinghistory



CREATE OR REPLACE VIEW SPSO_PRINTINGHISTORY AS

SELECT 

    "User".NAME, 

    "User".id AS USER_ID, -- Nếu bạn muốn phân biệt rõ ID này thuộc User

    PRINTER_ID,     -- Đổi tên PRINTER_ID thành ID

    FILE_TYPE, 

    FILE_NAME, 

    FILE_SIZE, 

    NO_PAGES, 

    STATUS, 

    TIME, 

    paper_orientation, 

    print_sides, 

    num_copies

FROM "User" 

JOIN "Uses" ON "User".USERNAME = "Uses".USERNAME

CREATE OR REPLACE VIEW spso_transaction AS
SELECT
    t.trans_id,
    t.price,
    t.no_pages,
    t.status AS transaction_status,
    u.username,
    u.name,
	u.id,
    s.account_balance
FROM 
    "Transaction" t
JOIN 
    "Student" s ON t.student_username = s.username
JOIN 
    "User" u ON s.username = u.username;

DROP VIEW spso_transaction

ALTER TABLE "Student" ALTER COLUMN "account_balance" SET DATA TYPE NUMERIC(10, 0);

delete from "Transaction"
where "status" = 'Lỗi Thanh Toán' 

---------------------------------------------------------------------------Thêm vào 8:57PM 12/12/2024
ALTER TABLE "Transaction"
ADD COLUMN time TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

CREATE OR REPLACE VIEW spso_transaction AS
SELECT
    t.trans_id,
    t.price,
    t.no_pages,
    t.status AS transaction_status,
    u.username,
    u.name,
	u.id,
    s.account_balance,
    t.time
FROM 
    "Transaction" t
JOIN 
    "Student" s ON t.student_username = s.username
JOIN 
    "User" u ON s.username = u.username;