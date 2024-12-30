// import "./Landingpage.css"


// const Landingpage = () => {
//     return (
//         <div className="landing-page">
//           <header className="landing-header">
//             <h1>Welcome to Alchemy Fusion</h1>
//             <p>Transforming creativity into reality.</p>
//             <button className="cta-button">Explore Now</button>
//       </header>
//     </div>
//     );
// };

// export default Landingpage;
// import { useNavigate } from "react-router-dom";
import "./Landingpage.css";
import { useModal } from "../../context/Modal";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";

export default function Landingpage() {

    const { setModalContent } = useModal();
    //const navigate = useNavigate();
    // const handleGetStarted = () => {
    //   console.log("Navigating to /home...");
    //   navigate("/home");
    //   };
    const handleSignupClick = () => {
      setModalContent(<SignupFormModal />);
    }
    const handleLoginClick = () => {
      setModalContent(<LoginFormModal />);
    }
  return (
    <div className="landing-page">
       <header className="landing-header">
      <h1>Welcome to Alchemy Fusion</h1>
      <p>Transforming creativity into reality.</p>
        <p>Your portal awaits.</p>
        <div className="landing-buttons">
          <button className="btn-get-started" onClick={handleSignupClick}>
            Get Started
          </button>
          <button className="btn-login" onClick={handleLoginClick}>
            Log In
          </button>
        </div>
      </header>
    </div>
  );
}
