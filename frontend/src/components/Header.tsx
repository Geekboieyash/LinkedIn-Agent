import React from 'react';
import '../styles/Header.css';

const Header: React.FC = () => {
  return (
    <header className="header">
      <div className="header-container">
        <div className="header-title">LinkedIn Post Generator</div>
        <nav>
          <ul className="header-nav">
            <li><a href="#" className="nav-link">Home</a></li>
            <li><a href="#" className="nav-link">Features</a></li>
            <li><a href="#" className="nav-link">About</a></li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;
