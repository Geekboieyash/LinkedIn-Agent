import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { tomorrow } from 'react-syntax-highlighter/dist/esm/styles/prism';
import remarkGfm from 'remark-gfm';
import remarkEmoji from 'remark-emoji';
import '../styles/PostGenerator.css'; 

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

  const handleGeneratePost = async () => {
    try {
      const response = await fetch('/api/linkedin/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic: code }),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      const data = await response.json();
      setGeneratedPost(data.content);
    } catch (error) {
      console.error('Failed to generate post:', error);
      alert('Failed to generate post. Please try again.');
    }
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
            <div className="mt-2">
              <ReactMarkdown
                remarkPlugins={[remarkGfm, remarkEmoji]}
                components={{
                  code({ node, inline, className, children, ...props }) {
                    const match = /language-(\w+)/.exec(className || '');
                    return !inline && match ? (
                      <SyntaxHighlighter
                        style={tomorrow}
                        language={match[1]}
                        PreTag="div"
                        {...props}
                      >
                        {String(children).replace(/\n$/, '')}
                      </SyntaxHighlighter>
                    ) : (
                      <code className={className} {...props}>
                        {children}
                      </code>
                    );
                  }
                }}
              >
                {generatedPost || 'Your LinkedIn post will appear here...'}
              </ReactMarkdown>
            </div>
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
