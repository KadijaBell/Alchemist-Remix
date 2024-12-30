import { useEffect, useState } from "react";
import { Outlet  } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { thunkAuthenticate } from "../redux/session";
import Navigation from "../components/Navigation/Navigation";
import { Modal, ModalProvider } from "../context/Modal";



export default function Layout() {
  const dispatch = useDispatch();
  //const navigate = useNavigate();
  const [isLoaded, setIsLoaded] = useState(false);
  const user = useSelector((state) => state.session.user);

  useEffect(() => {
    dispatch(thunkAuthenticate()).finally(() => setIsLoaded(true));
  }, [dispatch]);

  // useEffect(() => {
  //   if (isLoaded) {
  //     if (!user && window.location.pathname !== "/") {
  //       console.log("No user found, redirecting to landing page...");
  //       navigate("/", { replace: true });
  //     } else if (user && window.location.pathname === "/") {
  //       console.log("User logged in, redirecting to home...");
  //       navigate("/home", { replace: true });
  //     }
  //   }
  // }, [isLoaded, user, navigate]);

  if (!isLoaded) {
    return <div>Loading...🕳️</div>; // Show a loading state
  }

  return (
    <>
      <ModalProvider>
        {user && <Navigation />}
        <Outlet />
        <Modal />
      </ModalProvider>
    </>
  );
}
