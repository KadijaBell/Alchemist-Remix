import { useState } from "react";
import { useDispatch } from "react-redux";
import { thunkLogin } from "../../redux/session";
import { useModal } from "../../context/Modal";
import { useNavigate } from "react-router-dom";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});


  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});

    const serverResponse = await dispatch(thunkLogin({ email, password }));

    if (serverResponse?.errors) {
        setErrors(serverResponse.errors);
    } else {
      navigate("/home");
      closeModal();
    }
};
const handleDemoLogin = async () => {
  const demoEmail = "demo@example.com";
  const demoPassword = "Password1!";

  const serverResponse = await dispatch(
    thunkLogin({
      email: demoEmail,
      password: demoPassword,
    })
  );

  if (serverResponse.errors) {
    setErrors(serverResponse.errors);
  } else {
    closeModal();
    navigate("/home");
  }
};

  return (
    <>
      <h1>Log In</h1>
      <form onSubmit={handleSubmit} className="form-container">
        <label>
          Email
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        {errors.email && <p className="error-message">{errors.email}</p>}
        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        {errors.password && <p className="error-message">{errors.password}</p>}
        {errors.credentials && (
          <p className="error-message">{errors.credentials}</p>
        )}
        {errors.form && <p className="error-message">{errors.form}</p>}
        <button type="submit">Log In</button>
        <button type="button" onClick={handleDemoLogin}>Demo User</button>
      </form>
    </>
  );
}

export default LoginFormModal;
