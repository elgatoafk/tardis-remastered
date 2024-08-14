import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import '../styles/Navbar.css';

const Navbar = () => {
    const location = useLocation();
    const isOnAddSubtractPage = location.pathname === '/add-subtract';

    // Dark mode state
    const [darkMode, setDarkMode] = useState(false);

    // Load dark mode preference from local storage
    useEffect(() => {
        const savedMode = localStorage.getItem('darkMode') === 'true';
        setDarkMode(savedMode);
        document.body.classList.toggle('dark-mode', savedMode);
    }, []);

    const toggleDarkMode = () => {
        setDarkMode(!darkMode);
        document.body.classList.toggle('dark-mode', !darkMode);
        localStorage.setItem('darkMode', !darkMode);
    };

    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <div className="container-fluid justify-content-between">
                <h1 className="navbar-brand">Tardis Toolkit</h1>
                <div className="toggle-container">
                    <div className={`dark-mode-toggle ${darkMode ? 'dark' : 'light'}`} onClick={toggleDarkMode}>
                        <div className={`toggle-ball ${darkMode ? 'dark' : 'light'}`}>
                            <img
                                src={process.env.PUBLIC_URL + '/sun-icon.svg'}
                                alt="Sun icon"
                                className={`icon sun`}
                            />
                            <img
                                src={process.env.PUBLIC_URL + '/moon-icon.svg'}
                                alt="Moon icon"
                                className={`icon moon`}
                            />
                        </div>
                    </div>
                </div>
                <ul className="navbar-nav">
                    <li className="nav-item">
                        <Link to={isOnAddSubtractPage ? "/" : "/add-subtract"} className="nav-link">
                            {isOnAddSubtractPage ? "← Back" : "Add/Subtract Days →"}
                        </Link>
                    </li>
                </ul>
            </div>
        </nav>
    );
};

export default Navbar;
