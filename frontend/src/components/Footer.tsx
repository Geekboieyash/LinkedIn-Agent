import React from 'react';
import '../styles/Footer.css'
const Footer: React.FC = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-links">
          <a href="#" className="footer-link">Privacy Policy</a>
          <a href="#" className="footer-link">Terms of Service</a>
          <a href="#" className="footer-link">Contact Us</a>
        </div>
        <div className="footer-info">
          <p>© 2025 LinkedIn Post Generator. All rights reserved.</p>
          <p className="footer-tagline">Helping developers share their code on LinkedIn effectively.</p>
        </div>
      </div>
    </footer>  
  );
};

export default Footer;