
import { useSelector } from "react-redux";

function AboutMe() {
  const user = useSelector((store) => store.session.user);

  return (
    <div>
      <h1>About Me</h1>
      {user ? (
        <div>
          <p><strong>Username:</strong> {user.username}</p>
          <p><strong>Email:</strong> {user.email}</p>
          {/* Add fields for editing profile details */}
        </div>
      ) : (
        <p>Please log in to view your profile.</p>
      )}
    </div>
  );
}

export default AboutMe;
