import { useState } from "react";
//import { useDispatch } from "react-redux";
//import { createPostThunk } from "../../redux/posts";
import "./PostForm.css";
import { apiFetch } from "../../utils/api"; // Adjust the path as necessary

function PostForm() {
  //const dispatch = useDispatch();
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [media, setMedia] = useState(null);
  const [errors, setErrors] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("title", title);
    formData.append("content", content);
    formData.append("content_type", "text");
    if (media) formData.append("media", media);

    try {
      const response = await apiFetch("/api/posts/", "POST", formData);
      console.log(response);
    } catch (err) {
      setErrors([err.message]); 
    }
  };

  return (
    <form className="post-form" onSubmit={handleSubmit}>
      <h1>Create a New Post</h1>
      <ul>
        {errors.map((error, idx) => (
          <li key={idx}>{error}</li>
        ))}
      </ul>
      <label>
        Title
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
      </label>
      <label>
        Content
        <textarea
          value={content}
          onChange={(e) => setContent(e.target.value)}
          required
        />
      </label>
      <label>
        Media (optional)
        <input
          type="file"
          onChange={(e) => setMedia(e.target.files[0])}
        />
      </label>
      <button type="submit">Post</button>
    </form>
  );
}

export default PostForm;
