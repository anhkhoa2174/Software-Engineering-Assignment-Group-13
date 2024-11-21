import styled from 'styled-components';
import { Link } from 'react-router-dom';

export const NavbarContainer = styled.nav`
    width: 100%;
    height: 60px;
    background-color: var(--primary-red);
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 6%;
    position: fixed;
    top: 0;
    z-index: 10;
`;

// Logo styling
export const Logo = styled(Link)`
    color: white;
    text-decoration: none;
    font-size: 16px;
    font-family: var(--boundedFont);
    font-weight: bold;
    &:hover {
        color: #fae6e5;
    }
`;

// Menu items container
export const Menu = styled.li`
    display: flex;
    justify-content: right;
    @media (max-width: 768px) {
        display: ${({ isOpen }) => (isOpen ? 'flex' : 'none')};
        flex-direction: column;
        position: absolute;
        top: 60px;
        right: 0;
        background-color: #791b16;
        width: 100%;
        padding: 20px;
    }
`;

export const MenuItem = styled(Link)`
    color: white;
    text-decoration: none;
    position: relative;
    font-size: 20px;
    font-weight: 500;
    font-family: var(--boundedFont);
    background: var(--primary-red);
    display: block;
    padding: 15px 15px 15px 15px;
    ul {
        list-style: none;
    }
    ul li {
        display: inline-block;
        position: relative;
    }
    ul li a {
        display: block;
        padding: 10px 0 10px 0;
        margin: 5px;
        border-radius: 10px;
        background-color: #0a674f;
        text-decoration: none;
        text-align: center;
        font-size: 20px;
    }
    ul li ul.dropdown {
        width: 150%;
        background: #791B16;
        border-radius: 20px;
        transform: translate(-17.5%, 0);
        padding: 5%;
        position: absolute;
        z-index: 999;
        display: none;
    }
    ul li ul.dropdown li {
        display: block;
        align: center;
    }
    
    ul li a:hover {
        background-color: #1b493d;
    }
    ul:hover li ul.dropdown {
        display: block;
    }
    &:hover {
        color: #fae6e5;
        ul.dropdown {
            display: block;
        }
    }
`;

// Hamburger icon for mobile
export const HamburgerIcon = styled.div`
    display: none;
    cursor: pointer;

    @media (max-width: 768px) {
        display: block;
    }

    span {
        display: block;
        width: 25px;
        height: 3px;
        background-color: white;
        margin: 5px 0;
    }
`;

export const SearchContainer = styled.div`
    display: flex;
    align-items: center;
    flex: 1;
    margin-left: 2rem;
`;

export const SearchInput = styled.input`
    width: 100%;
    padding: 12px;
    border-radius: 4px;
    border: none;
    outline: none;
    font-size: 0.85rem;
    font-family: var(--boundedFont);
    transition: width 0.3s ease;
    @media (max-width: 767px) {
        width: 90%;
        max-width: 200px;
    }
    @media (min-width: 768px) {
        width: 90%;
        max-width: 300px;
    }
`;
