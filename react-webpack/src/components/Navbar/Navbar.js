import React, { useState } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { Menu, MenuItem, NavbarContainer } from './Navbar.style';

const Navbar = (props) => {
    const [isOpen, setIsOpen] = useState(false);
    //const [isMobile, setIsMobile] = useState(false); // Track mobile view

    const toggleMenu = () => {
        setIsOpen(!isOpen);
    };

    return (
        <NavbarContainer>
            <Logo to="/">MyLogo</Logo>
            <HamburgerIcon onClick={toggleMenu}>
                <span></span>
                <span></span>
                <span></span>
            </HamburgerIcon>
            <Menu isOpen={isOpen}>
                <MenuItem to="/">
                    TRANG CHỦ
                </MenuItem>
                <MenuItem to="/dashboard">
                    <ul>
                        <li>Categories
                            <ul class="dropdown">
                                <li><a>Action</a></li>
                                <li><a>Crime</a></li>
                                <li><a>Horror</a></li>
                                <li><a>Drama</a></li>
                                <li><a>Fantasy</a></li>
                                <li><a>Comedy</a></li>
                                <li><a>Mystery</a></li>
                            </ul>
                        </li>
                    </ul>
                </MenuItem>
                <MenuItem to="/print-document">IN TÀI LIỆU</MenuItem>
                <MenuItem to="/printing-log">LỊCH SỬ IN</MenuItem>
                <MenuItem to="/buy-more-paper">MUA THÊM GIẤY</MenuItem>
            </Menu>
        </NavbarContainer>
    );
};

export default Navbar;