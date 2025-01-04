import { useDispatch, useSelector } from "react-redux";
import { thunkCreatePost } from "../../redux/posts";
import { useState } from "react";
import { Navigate } from "react-router-dom";

function CreatePost() {
  const dispatch = useDispatch();
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [contentType, setContentType] = useState("Text");
  const [media, setMedia] = useState(null);
  const user = useSelector((state) => state.session.user);
  const error = useSelector((state) => state.posts.error);

  if (!user) {
    return <Navigate to="/login" />;
  }

  // const handleSubmit = async (e) => {
  //   e.preventDefault();

  //   const formData = new FormData();
  //   formData.append("title", title);
  //   formData.append("content", content);
  //   formData.append("contentType", contentType);
  //   if (media) {
  //     formData.append("media", media);
  //   }

  //   await dispatch(createPostThunk(formData));
  // };
  const handleSubmit = async (e) => {
    e.preventDefault();
    const post = { title, content, contentType, media };
    console.log("Post object being sent:", post);

    const response = await dispatch(thunkCreatePost(post));
    if (response?.errors) {
      console.error("Error creating post:", response.errors);
    }
  };


  return (
    <div>
      <h1>Create Post</h1>
      {error?.message && (<p style={{ color: "red" }}> <strong>{error.message}</strong> Try adjusting your formula and conjuring again! 🔮
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
            <option value="">Select Content Type</option>
            <option value="Text">Text</option>
            <option value="Podcast">Podcast</option>
            <option value="Video">Video</option>
            <option value="Image">Image</option>
          </select>
        </label>
        <label>
          Media (optional):
          <input type="file" onChange={(e) => setMedia(e.target.files[0])} />
        </label>
        <button type="submit">Create Post</button>
      </form>
    </div>
  );
}

export default CreatePost;
