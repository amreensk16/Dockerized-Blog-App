import React, { useEffect, useState } from "react";

function App() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/posts/json") // Flask backend API
      .then((res) => res.json())
      .then((data) => setPosts(data))
      .catch((err) => console.error("Error:", err));
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Blog Posts</h1>
      <ul>
        {posts.map((post, i) => (
          <li key={i}>
            <strong>{post.title}</strong>: {post.content}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
