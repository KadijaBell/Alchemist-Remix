import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { fetchFeed } from "../../redux/feed";
import PostCard from "../Post/PostContainer";
import "./Feed.css";

function Feed() {
  const dispatch = useDispatch();
  const { list: posts, status, error, total_pages } = useSelector((state) => state.posts);
  const user = useSelector((state) => state.session.user);
  const navigate = useNavigate();
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    if (user) {
      dispatch(fetchFeed(currentPage));
    } else {
      navigate("/login");
    }
  }, [dispatch, currentPage, user, navigate]);

  const handleNextPage = () => {
    if (currentPage < total_pages) {
      setCurrentPage(currentPage + 1);
    }
  };

  const handlePreviousPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  if (status === "loading") {
    return <p>✨ Brewing your feed... Please wait while the magic unfolds! 🔮</p>;
  }

  if (status === "failed") {
    return <p>🥲 Oops! The cauldron spilled while conjuring your feed: {error} 🌌</p>;
  }

  // if (posts.length === 0) {
  //   return (
  //     <div className="feed-container">
  //       <h1>Your Alchemy Feed</h1>
  //       <p>No content found. Start creating or exploring new sources! 🪄</p>
  //     </div>
  //   );
  // }

  return (
    <div className="feed-container">
      <h1>Your Alchemy Feed</h1>
      <button className="create-post-button" onClick={() => navigate("/create")}> + Create Post </button>
      <div className="posts-list">
        {posts.map((post) => (
          <PostCard key={post.id} post={post} />
        ))}
      </div>
      <div className="pagination-controls">
        <button onClick={handlePreviousPage} disabled={currentPage === 1}>
          Previous
        </button>
        <span>Page {currentPage} of {total_pages}</span>
        <button onClick={handleNextPage} disabled={currentPage === total_pages}>
          Next
        </button>
      </div>
    </div>
  );
}

export default Feed;

