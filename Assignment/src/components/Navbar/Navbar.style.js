import styled from 'styled-components';
import { Link } from 'react-router-dom';

export const NavbarContainer = styled.nav`
    width: 100%;
    height: 65px;
    color: white;
    display: flex;
    background: #23abea;
    justify-content: space-between;
    align-items: center;
    position: fixed;
    top: 0;
    box-shadow: 0px 3.2px 3.2px #666565e6;
    z-index: 999
`;

// Logo styling
export const LogoBox = styled.div`
    width: 255px;
    height: 53.6px;
    left: 57.6px;
    top: 5.6px;
    position: absolute;
    background: #142c64;
    border-radius: 15px;
    justify-content: right;
`;

// Menu items container
export const Menu = styled.div`
    width: 60%;
    height: 100%;
    left: 320px;
    position: absolute;
    align-items: center;
    display: inline-flex;
    &&:hover {
        color: #fae6e5;
        ul.dropdown {
            display: block;
        }
    }
`;

export const MenuItem = styled(Link)`
    color: #142c64;
    height: 100%;
    text-decoration: none;
    align-items: center;
    position: relative;
    font-size: 20px;
    font-weight: 500;
    font-family: var(--boundedFont);
    display: flex;
    padding: 0 20px 0 20px;
    &&:hover {
        background-color: #142c64;
        color: #FFFFFF
    }
`;

export const InfoList = styled.ul`
    height: 100%;
    position: absolute;
    align-items: center;
    display: inline-flex;
    background: #23abea;
    li {
        position: absolute;
        align-items: center;
        display: inline-flex;
        flex-direction: row;
        position: relative;
    }
    li ul.dropdown {
        width: 150%;
        color: #000000;
        background: #ffffff;
        transform: translate(-17.5%, 65%);
        padding: 0;
        position: absolute;
        z-index: 999;
        display: none;
        border: #000000 1px solid;
        border-radius: 10px;
    }
    li ul.dropdown li {
        display: block;
        align: center;
        padding: 10px 0 10px 10px;
        text-decoration: none;
        text-align: left;
        font-size: 20px;
        border-radius: 10px;
    }
    
    li ul.dropdown li ul.nextpage {
        width: 100%;
        color: #000000;
        background: #ffffff;
        transform: translate(-17.5%, 65%);
        padding: 0;
        position: absolute;
        z-index: 999;
        display: none;
        border: #000000 1px solid;
        border-radius: 10px;
    }

    li ul.dropdown li ul.nextpage li:onlick {
        display: block;
    }

    li ul.dropdown li:hover {
        background-color: #cbcbcb;
        display: block;
    }
    &&:hover li ul.dropdown {
        display: block;
    }
`;

export const Info = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: right;
    position: absolute;
    width: 200px;
    height: 100%;
    right: 3%;
    align-items: center;
    padding: 0 2% 0 0;
`;

export const Noti = styled.div`
    height: 100%;
    left: 5%;
    position: absolute;
`;

export const Name = styled.div`
    font-size: 15px;
    font-family: Montserrat, sans-serif;
    font-weight: 400;
    color: black;
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
