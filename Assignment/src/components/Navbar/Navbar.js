import React from 'react';
import { Info, InfoList, LogoBox, Menu, MenuItem, Name, NavbarContainer, Noti } from './Navbar.style';
import logoBK from "./01_logobachkhoatoi 1.png"
const Navbar = (props) => {

    return (
        <NavbarContainer>
            <LogoBox>
                <img
                    style={{
                        width: "35%",
                        left: "-7%",
                        top: "0.8px",
                        position: "absolute",
                        float: "left"
                    }}
                    src={logoBK} />
                <div
                    style={{
                        width: "70%",
                        position: "absolute",
                        left: "25%",
                        color: "white",
                        fontSize: "22px",
                        fontFamily: "Montserrat",
                        fontWeight: "700",
                        wordWrap: "break-word",
                        float: "right"
                    }}>
                    Student Smart Printing Service
                </div>
            </LogoBox>
            <Menu>
                <MenuItem to='/'>TRANG CHỦ</MenuItem>
                <MenuItem>BẢNG ĐIỀU KHIỂN</MenuItem>
                <MenuItem>IN TÀI LIỆU</MenuItem>
                <MenuItem>LỊCH SỬ IN</MenuItem>
                <MenuItem>MUA THÊM GIẤY</MenuItem>
            </Menu>
            <Info>
                <Noti>
                    <svg style={{ position: 'absolute', top: '50%', transform: 'translate(60%, -50%)' }}
                        width="20"
                        height="20"
                        viewBox="0 0 20 20"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg">
                        <path
                            id="Vector"
                            d="M12 15V16C12 17.6569 10.6569 19 9 19C7.34315 19 6 17.6569 6 16V15M12 15H6M12 15H15.5905C15.973 15 16.1652 15 16.3201 14.9478C16.616 14.848 16.8475 14.6156 16.9473 14.3198C16.9997 14.1643 16.9997 13.9715 16.9997 13.5859C16.9997 13.4172 16.9995 13.3329 16.9863 13.2524C16.9614 13.1004 16.9024 12.9563 16.8126 12.8312C16.7651 12.7651 16.7048 12.7048 16.5858 12.5858L16.1963 12.1963C16.0706 12.0706 16 11.9001 16 11.7224V8C16 4.134 12.866 0.999991 9 1C5.13401 1.00001 2 4.13401 2 8V11.7224C2 11.9002 1.92924 12.0706 1.80357 12.1963L1.41406 12.5858C1.29476 12.7051 1.23504 12.765 1.1875 12.8312C1.09766 12.9564 1.03815 13.1004 1.0132 13.2524C1 13.3329 1 13.4172 1 13.586C1 13.9715 1 14.1642 1.05245 14.3197C1.15225 14.6156 1.3848 14.848 1.68066 14.9478C1.83556 15 2.02701 15 2.40956 15H6"
                            stroke="black"
                            stroke-width="1.6"
                            stroke-linecap="round"
                            stroke-linejoin="round" />
                    </svg>
                    <svg style={{ position: 'absolute', top: '50%', transform: 'translate(0, -50%)' }}
                        width="42"
                        height="42"
                        viewBox="0 0 42 42"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg">
                        <path
                            id="Ellipse 3230"
                            d="M41 20.5C41 31.5457 32.0457 40.5 21 40.5C9.9543 40.5 1 31.5457 1 20.5C1 9.4543 9.9543 0.5 21 0.5C32.0457 0.5 41 9.4543 41 20.5Z"
                            stroke="black" />
                    </svg>
                </Noti>
                <InfoList>
                    <li>
                        <svg
                            width="51"
                            height="51"
                            viewBox="0 0 51 51"
                            fill="none"
                            xmlns="http://www.w3.org/2000/svg">
                            <g id="User / User_Square">
                                <path
                                    id="Vector"
                                    d="M35.6998 44.0998C35.6998 38.3008 30.9988 33.5998 25.1998 33.5998C19.4008 33.5998 14.6998 38.3008 14.6998 44.0998M35.6998 44.0998H37.3863C39.7339 44.0998 40.9078 44.0998 41.8053 43.6425C42.5956 43.2398 43.2398 42.5956 43.6425 41.8053C44.0998 40.9078 44.0998 39.7339 44.0998 37.3863V13.0133C44.0998 10.6657 44.0998 9.49013 43.6425 8.59258C43.2398 7.8023 42.5956 7.16025 41.8053 6.75758C40.9069 6.2998 39.7324 6.2998 37.3802 6.2998H13.0202C10.668 6.2998 9.49101 6.2998 8.59258 6.75758C7.8023 7.16025 7.16025 7.8023 6.75758 8.59258C6.2998 9.49101 6.2998 10.668 6.2998 13.0202V37.3802C6.2998 39.7324 6.2998 40.9069 6.75758 41.8053C7.16025 42.5956 7.8023 43.2398 8.59258 43.6425C9.49013 44.0998 10.6657 44.0998 13.0133 44.0998H14.6998M35.6998 44.0998H14.6998M25.1998 27.2998C21.7204 27.2998 18.8998 24.4792 18.8998 20.9998C18.8998 17.5204 21.7204 14.6998 25.1998 14.6998C28.6792 14.6998 31.4998 17.5204 31.4998 20.9998C31.4998 24.4792 28.6792 27.2998 25.1998 27.2998Z"
                                    stroke="black"
                                    stroke-width="1.6"
                                    stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </g>
                        </svg>
                        <Name>
                            Katheryn
                        </Name>
                        <ul class="dropdown">
                            <li><a>Hồ sơ</a></li>
                            <li>
                                <a>Ngôn ngữ</a>
                                <ul class="nextpage">
                                    <li>Tiếng Việt</li>
                                    <li>English</li>
                                </ul>
                            </li>
                            <li><a>Đăng xuất</a></li>
                        </ul>
                    </li>
                </InfoList>
            </Info>
        </NavbarContainer>
    );
};

export default Navbar;
