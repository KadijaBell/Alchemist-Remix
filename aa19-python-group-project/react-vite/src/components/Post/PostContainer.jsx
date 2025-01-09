import './PostContainer.css';

 function PostCard({ post }) {
  console.log("PostContainer Post Data:", post);
  //const { title, content, content_type, media:mediaType, url } = post;
  // const renderPreview = () => {
  //   switch (mediaType?.toLowerCase()) {
  //     case "image":
  //       return url ? <img src={url} alt={title} /> : <p>No image available</p>;
  //     case "video":
  //       return (
  //         <video controls>
  //           <source src={url} type="video/mp4" />
  //           Your browser does not support the video element.
  //         </video>
  //       );
  //     default:
  //       return <p>No preview available</p>;
  //   }
  // };
  console.log("PostContainer Post Data:", post);

  return (
    <div className="post-container">
      {/* {renderPreview()} */}
        <h2>{post.title || "Untitled"}</h2>
        <p>{post.content || "No content available."}</p>
        <p>{post.content_type && <p>Content Type: {post.content_type}</p>}</p>
        <a href={post.url} target="_blank" rel="noreferrer">
        Visit Source
      </a>
      </div>
  );
}
// import { useDispatch } from "react-redux";
// import { thunkDeletePost } from "../../redux/posts";
// import { useNavigate } from "react-router-dom";

// function PostCard({ post }) {
//   const dispatch = useDispatch();
//   const navigate = useNavigate();

//   const handleDelete = () => {
//     if (window.confirm("Are you sure you want to delete this post?")) {
//       dispatch(thunkDeletePost(post.id));
//     }
//   };
//   const handleEdit = () => {
//     navigate(`/edit/${post.id}`);
//   };


//   return (
//     <div className="post-card">
//       <h2>{post.title}</h2>
//       <p>{post.content}</p>
//       <p><strong>Type:</strong> {post.content_type}</p>
//       <button onClick={handleEdit}>✏️ Edit</button>
//       <button onClick={handleDelete}>🧪 Delete Post</button>
//     </div>
//   );
// }

export default PostCard;
