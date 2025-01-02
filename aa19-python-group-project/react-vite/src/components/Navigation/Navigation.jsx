import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

// function Navigation() {
//   return (
//     <ul>
//       <li>
//         <NavLink to="/">Home</NavLink>
//       </li>

//       <li>
//         <ProfileButton />
//       </li>
//     </ul>
//   );
// }

// export default Navigation;
function Navigation() {
  const links = [
    { to: "/", label: "Home" },
    { to: "/feed", label: "Feed" },
    { to: "/create-post", label: "Create Post" },
    { to: "/about-me", label: "About Me" },
  ];

  return (
    <nav className="navbar">
      <ul className="nav-links">
        {links.map((link) => (
          <li key={link.to}>
            <NavLink to={link.to} activeClassName="active-link">
              {link.label}
            </NavLink>
          </li>
        ))}
        <li>
          <ProfileButton />
        </li>
      </ul>
    </nav>
  );
}

export default Navigation;
