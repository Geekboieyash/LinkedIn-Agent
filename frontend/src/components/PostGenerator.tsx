import React, { useState } from 'react';

const PostGenerator: React.FC = () => {
  const [code, setCode] = useState('');
  const [generatedPost, setGeneratedPost] = useState('');

  const handleInputChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setCode(e.target.value);
  };

  const handleGeneratePost = () => {
    // Placeholder logic – replace this with actual API call or logic
    const fakePost = `🚀 Just wrote this code snippet:

\`\`\`ts
${code}
\`\`\`

Loving how it turned out! 🔥 #DevLife #React #TypeScript`;
    setGeneratedPost(fakePost);
  };

  return (
    <div className="flex flex-col md:flex-row gap-6 w-full max-w-screen-xl mx-auto">
      {/* Input Section */}
      <div className="w-full md:w-1/2 bg-white shadow-md rounded-xl overflow-hidden p-4">
        <h2 className="text-lg font-semibold bg-blue-700 text-white p-2 rounded">Input Your Code</h2>
        <textarea
          className="w-full h-64 mt-4 p-3 rounded bg-[#1e1e1e] text-gray-200 font-mono resize-none"
          placeholder="Paste your code snippet here..."
          value={code}
          onChange={handleInputChange}
        />
        <button
          onClick={handleGeneratePost}
          className="mt-4 bg-blue-700 text-white px-4 py-2 rounded hover:bg-blue-800 transition"
        >
          Generate LinkedIn Post
        </button>
      </div>

      {/* Output Section */}
      <div className="w-full md:w-1/2 bg-white shadow-md rounded-xl overflow-hidden p-4">
        <h2 className="text-lg font-semibold bg-blue-700 text-white p-2 rounded">Generated LinkedIn Post</h2>
        <div className="mt-4 whitespace-pre-wrap text-gray-700 italic min-h-[16rem]">
          {generatedPost || 'Your LinkedIn post will appear here...'}
        </div>
      </div>
    </div>
  );
};

export default PostGenerator;
