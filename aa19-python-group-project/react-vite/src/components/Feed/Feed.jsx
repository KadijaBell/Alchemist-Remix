import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
//import { fetchFusions} from '../../redux/fusions';
import { fetchFeed } from '../../redux/feed';
import PostCard from '../Post/PostContainer';
import './Feed.css';

// function Feed() {
//   const dispatch = useDispatch();
//   const { list: posts, status, error } = useSelector((state) => state.feed);

//   useEffect(() => {
//     if (status === 'idle') {
//       dispatch(fetchFeed());
//     }
//   }, [dispatch, status]);

//   if (status === 'loading') {
//     return <p>✨ Brewing your feed... Please wait while the magic unfolds! 🔮</p>;
//   }

//   if (status === 'failed') {
//     return (
//       <p>
//         🥲 Oops! The cauldron spilled while conjuring your feed: {error}.🌌
//       </p>
//     );
//   }

//   return (
//     <div>
//       <h1>Your Alchemy Feed</h1>
//         <p>Discover the magic of Alchemy Fusion in your feed. Here&apos;s what&apos;s brewing...</p>
//         <div className="posts-list">
//             {posts.map((post) => (
//                 <PostCard
//                 key={post.id}
//                 title={post.title}
//                 content={post.content}
//                 contentType={post.content_type}
//                 metadata={post.metadata}
//                 mediaType={post.media_type}
//                 url={post.url}
//               />
//             ))}
// </div>

//     </div>
//   );
// }

// export default Feed;
function Feed() {
  const dispatch = useDispatch();
  const { list: posts, status, error } = useSelector((state) => state.feed);

  useEffect(() => {
    if (status === 'idle') {
      dispatch(fetchFeed());
    }
  }, [dispatch, status]);

  if (status === 'loading') {
    return <p>✨ Brewing your feed... Please wait while the magic unfolds! 🔮</p>;
  }

  if (status === 'failed') {
    return (
      <p>
        🥲 Oops! The cauldron spilled while conjuring your feed: {error}.🌌
      </p>
    );
  }

  return (
    <div className="feed-container">
      <h1>Your Alchemy Feed</h1>
      <p>Discover the magic of Alchemy Fusion in your feed. Here&apos;s what&apos;s brewing...</p>
      <div className="posts-list">
        {posts.map((post) => (
          <PostCard
            key={post.id}
            title={post.title}
            content={post.content}
            contentType={post.content_type}
            metadata={post.metadata}
            mediaType={post.media_type}
            url={post.url}
          />
        ))}
      </div>
      <button className="fab" onClick={() => dispatch(fetchFeed())}>
        +
      </button>
    </div>
  );
}

export default Feed;
