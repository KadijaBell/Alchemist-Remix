import "./ErrorModal.css";

function ErrorModal({ errors, onClose }) {
  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h2>Error</h2>
        <ul>
          {errors.map((error, index) => (
            <li key={index}>{error}</li>
          ))}
        </ul>
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
}

export default ErrorModal;
