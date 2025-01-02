import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkSignup } from "../../redux/session";
import { useNavigate } from "react-router-dom";
import "./SignupForm.css";

function SignupFormModal() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { closeModal } = useModal();
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState({});

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});

    if (password !== confirmPassword) {
      setErrors({
        email: "✨ This email is already in use. Choose another or recover your account.",
        username: "✨ This username is already in use. Choose another.",
        password: "Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>).",
        confirmPassword: "✨ Your passwords must align to unlock the fusion portal! Try again.",
      });
      return
    }

    const serverResponse = await dispatch(
    thunkSignup({
      email,
      username,
      password,
    })
  );

    if (serverResponse.errors) {
      setErrors(serverResponse.errors);
    } else {
      closeModal();
      navigate("/home");
    }



    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  };

  return (
    <>
      <h1>Sign Up</h1>
      {errors.server && <p>🧙‍♂️ {errors.server}🧝🏾‍♀️</p>}
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
        {errors.email && <p className ="error-message">💎{errors.email}💎</p>}
        <label>
          Username
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>
        {errors.username && <p className ="error-message">✨{errors.username}✨</p>}
        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        {errors.password && <p className ="error-message">🔮{errors.password}🔮</p>}

        <label>
          Confirm Password
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
        </label>
        {errors.confirmPassword && <p className ="error-message">🧪{errors.confirmPassword}🧪</p>}
        <button type="submit">Sign Up</button>
      </form>
    </>
  );
}

export default SignupFormModal;
