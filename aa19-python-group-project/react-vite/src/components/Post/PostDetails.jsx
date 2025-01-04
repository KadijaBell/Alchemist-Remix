import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

function PostDetails() {
  const { id } = useParams();
  const [post, setPost] = useState(null);

  useEffect(() => {
    async function fetchPost() {
      const response = await fetch(`/api/posts/${id}`);
      const data = await response.json();
      setPost(data);
    }
    fetchPost();
  }, [id]);

  if (!post) return <p>Loading post details...🔮</p>;

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
      {post.media && <img src={post.media} alt={post.title} />}
    </div>
  );
}

export default PostDetails;
