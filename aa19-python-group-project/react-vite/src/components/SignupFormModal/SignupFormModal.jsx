import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkSignup } from "../../redux/session";
import { useNavigate } from "react-router-dom";
import ErrorModal from "../Modals/Errors/ErrorModal";
import "./SignupForm.css";

function SignupFormModal() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { closeModal, setModalContent } = useModal();
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  //const errors = useState({});


  const validatePassword = (password) => {
    const errors = [];
    if (password.length < 8) errors.push("Password must be at least 8 characters long.");
    if (!/[A-Z]/.test(password)) errors.push("Password must contain at least one uppercase letter.");
    if (!/[a-z]/.test(password)) errors.push("Password must contain at least one lowercase letter.");
    if (!/[0-9]/.test(password)) errors.push("Password must contain at least one digit.");
    if (!/[!@#$%^&*(),.?\\":{}|<>]/.test(password)) errors.push("Password must contain at least one special character.");
    return errors;
  };


  const handleSubmit = async (e) => {
    e.preventDefault();

    const passwordErrors = validatePassword(password);
    if (passwordErrors.length > 0) {
      setModalContent(<ErrorModal errors={passwordErrors} onClose={closeModal} />);
      return;
    }

    if (password !== confirmPassword) {
      setModalContent(<ErrorModal errors={{ confirmPassword: "Confirm Password field must be the same as the Password field" }} onClose={closeModal} />);
      return;
    // if (password !== confirmPassword) {
    //   return setErrors({
    //     password: "Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>).",
    //     confirmPassword: "✨ Your passwords must align to unlock the fusion portal! Try again.",
    //   });

    }

    const serverResponse = await dispatch(
    thunkSignup({
      email,
      username,
      password,
    })
  );


  if (serverResponse.errors) {
    setModalContent(<ErrorModal errors={serverResponse.errors} onClose={closeModal} />);
  } else {
    closeModal();
    navigate("/");
  }
};

return (
  <>
    <h1>Sign Up</h1>
    <form onSubmit={handleSubmit} className="form-container">
      <label>
        Email
        <input
          type="text"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </label>
      <label>
        Username
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
      </label>
      <label>
        Password
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </label>
      <label>
        Confirm Password
        <input
          type="password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          required
        />
      </label>
      <button type="submit">Sign Up</button>
    </form>
  </>
);
}
//   return (
//     <>
//       <h1>Sign Up</h1>
//       {errors.server && <p>🧙‍♂️ {errors.server}🧝🏾‍♀️</p>}
//       <form onSubmit={handleSubmit} className="form-container">
//         <label>
//           Email
//           <input
//             type="text"
//             value={email}
//             onChange={(e) => setEmail(e.target.value)}
//             required
//           />
//         </label>
//         {errors.email && <p className ="error-message">💎{errors.email}💎</p>}
//         <label>
//           Username
//           <input
//             type="text"
//             value={username}
//             onChange={(e) => setUsername(e.target.value)}
//             required
//           />
//         </label>
//         {errors.username && <p className ="error-message">✨{errors.username}✨</p>}
//         <label>
//           Password
//           <input
//             type="password"
//             value={password}
//             onChange={(e) => setPassword(e.target.value)}
//             required
//           />
//         </label>
//         {errors.password && <p className ="error-message">🔮{errors.password}🔮</p>}

//         <label>
//           Confirm Password
//           <input
//             type="password"
//             value={confirmPassword}
//             onChange={(e) => setConfirmPassword(e.target.value)}
//             required
//           />
//         </label>
//         {errors.confirmPassword && <p className ="error-message">🧪{errors.confirmPassword}🧪</p>}
//         <button type="submit">Sign Up</button>
//       </form>
//     </>
//   );
// }

export default SignupFormModal;
