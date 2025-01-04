import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import { useSelector } from "react-redux";
import "./Navigation.css";

function Navigation() {
  const user = useSelector((store) => store.session.user);


 return (
    <ul>
      {user ? (
        <>
          <li><NavLink to="/home">Home</NavLink></li>
          <li><NavLink to="/feed">Feed</NavLink></li>
          <li><NavLink to="/create">Create Post</NavLink></li>
          <li><NavLink to="/profile">About Me</NavLink></li>
          <ProfileButton />
        </>
      ) : (
        <li>
          <NavLink to="/login">Log In</NavLink>
          <NavLink to="/">Home</NavLink>
        </li>
      )}
    </ul>
  );
}

export default Navigation;
