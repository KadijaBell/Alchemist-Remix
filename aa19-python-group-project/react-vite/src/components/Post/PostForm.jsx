import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkCreatePost } from "../../redux/posts";
import { useNavigate } from "react-router-dom";
import "./PostForm.css";

function PostForm() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [contentType, setContentType] = useState("Text");
  const [media, setMedia] = useState(null);
  const [url, setUrl] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const error = useSelector((state) => state.posts.error);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);

    const formData = new FormData();
    formData.append("title", title);
    formData.append("content", content);
    formData.append("content_type", contentType);
    if (media) {
      formData.append("media", media);
    }
    if (url) {
      formData.append("url", url);
    }

    const response = await dispatch(thunkCreatePost(formData));
    if (response?.errors) {
      console.error("Error creating post:", response.errors);
    } else {
      navigate("/feed");
    }
    setIsSubmitting(false);
  };

  return (
    <div>
      <h1>Create Post</h1>
      {error?.message && (
        <p style={{ color: "red" }}>
          <strong>{error.message}</strong> Try adjusting your formula and conjuring again! 🔮
        </p>
      )}
      <form onSubmit={handleSubmit}>
        <label>
          Title:
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </label>
        <label>
          Content:
          <textarea
            value={content}
            onChange={(e) => setContent(e.target.value)}
          />
        </label>
        <label>
          Content Type:
          <select
            value={contentType}
            onChange={(e) => setContentType(e.target.value)}
          >
            <option value="Text">Text</option>
            <option value="Podcast">Podcast</option>
            <option value="Video">Video</option>
            <option value="Image">Image</option>
            <option value="Audio">Audio</option>
            <option value="Article">Article</option>
            <option value="Book">Book</option>
            <option value="Other">Other</option>
          </select>
        </label>
        {contentType === "Link" && (
          <label>
            URL:
            <input
              type="url"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
            />
          </label>
        )}
        {["Image", "Audio", "Video"].includes(contentType) && (
          <label>
            Media (optional):
            <input type="file" onChange={(e) => setMedia(e.target.files[0])} />
          </label>
        )}
        <button type="submit" disabled={isSubmitting}>
          {isSubmitting ? "Creating Post..." : "Transport 🔮"}
        </button>
      </form>
    </div>
  );
}

export default PostForm;
