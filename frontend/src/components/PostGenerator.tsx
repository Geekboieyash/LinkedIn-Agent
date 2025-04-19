import React, { useState } from 'react';
import '../styles/PostGenerator.css'
const PostGenerator: React.FC = () => {
  const [code, setCode] = useState('');
  const [generatedPost, setGeneratedPost] = useState('');

  // Placeholder user info
  const [userName] = useState('Your Name');
  const [userTitle] = useState('Your Title');
  const [userCompany] = useState('Your Company');

  const handleInputChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setCode(e.target.value);
  };

  const handleGeneratePost = () => {
    const fakePost = `🚀 Just wrote this code snippet:

\`\`\`ts
${code}
\`\`\`

Loving how it turned out! 🔥 #DevLife #React #TypeScript`;
    setGeneratedPost(fakePost);
  };

  const handleCopyToClipboard = () => {
    if (generatedPost && navigator.clipboard) {
      navigator.clipboard.writeText(generatedPost)
        .then(() => alert('Copied to clipboard!'))
        .catch(err => console.error('Failed to copy text: ', err));
    }
  };

  return (
    <div className="app-container">
      <h1>LinkedIn Post Generator</h1>
      <p>Transform your code into engaging LinkedIn posts using AI</p>

      <div className="content">
        <div className="input-container">
          <h2>Input Your Code</h2>
          <textarea
            className="code-input"
            placeholder="Paste your code snippet here..."
            value={code}
            onChange={handleInputChange}
          />
          <button onClick={handleGeneratePost} className="generate-button">
            Generate LinkedIn Post
          </button>
        </div>

        <div className="post-container">
          <h2>Generated LinkedIn Post</h2>
          <div className="post-preview">
            <div className="font-bold">{userName}</div>
            <div className="text-sm text-gray-600">{userTitle} • {userCompany}</div>
            <div className="mt-2">{generatedPost || 'Your LinkedIn post will appear here...'}</div>
          </div>
          <button onClick={handleCopyToClipboard} className="copy-button">
            Copy to Clipboard
          </button>
        </div>
      </div>
    </div>
  );
};

export default PostGenerator;
