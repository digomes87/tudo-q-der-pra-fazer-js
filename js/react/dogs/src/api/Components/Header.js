import React from 'react'
import style from './Header.module.css'
import { Link } from 'react-router-dom'
import { ReactComponent as Dogs } from '../Assets/dogs.svg'

const Header = () => {
    return(
        <header className={style.header}>
            <nav className={`${style.nav} container`}>
                <Link classname={style.logo}  to="/" aria-label="Dogs"><Dogs /></Link>
                <Link className={style.login} to="/login">Login / Criar</Link>
            </nav>
        </header>
    )
};

export default Header;
