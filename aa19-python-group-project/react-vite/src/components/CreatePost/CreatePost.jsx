import PostForm from "../Post/PostForm";
import { useSelector } from "react-redux";

function CreatePost() {
  
  const user = useSelector((state) => state.session.user);
  return (
    <div className="create-post-container">
      <h1>{user?.username || "Guest"}, Create a post!</h1>
      <PostForm />
    </div>
  );
}

export default CreatePost;
