import './PostContainer.css';

function PostCard({ title, content, contentType, metadata, mediaType, url }) {
  const renderPreview = () => {
    switch (mediaType?.toLowerCase()) {
      case 'video':
        return (
          <video className="media-preview" controls>
            <source src={url} type="video/mp4" />
            Your browser does not support the video element.
          </video>
        );
      case 'podcast':
        return (
          <audio className="media-preview" controls>
            <source src={url} type="audio/mpeg" />
            Your browser does not support the audio element.
          </audio>
        );
      case 'image':
        return <img className="media-preview" src={url} alt={title} />;
      default:
        return (
          <div className="media-placeholder">
            <span>🔗</span> {/* Placeholder icon */}
            <p>No preview available</p>
          </div>
        );
    }
  };

  return (
    <div className="post-card">
      {renderPreview()}
      <div className="post-content">
        <h2>{title}</h2> 
        <p>Type: {contentType}</p>
        <p>Link: {metadata || "None"}</p>
        <p>{content}</p>
        <a href={url} target="_blank" rel="noreferrer" className="visit-link">
          Visit Source
        </a>
      </div>
    </div>
  );
}

export default PostCard;
