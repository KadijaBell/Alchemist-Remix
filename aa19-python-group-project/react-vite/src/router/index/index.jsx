import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../../components/LoginFormPage';
import SignupFormPage from '../../components/SignupFormPage';
import Homepage from '../../components/Homepage/Homepage.jsx';
import Landingpage from '../../components/Landingpage/Landingpage.jsx';
import Feed from '../../components/Feed/Feed.jsx';
import CreatePost from '../../components/CreatePost/CreatePost.jsx';
import AboutMe from '../../components/AboutMe/AboutMe.jsx';
import Layout from '../Layout';
import './index.css';


export const router = createBrowserRouter([

  {
    path: "/",
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <Landingpage />,
      },
      {
        path: "/home",
        element: <Homepage />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "/feed",
        element: <Feed />,
      },
      {
        path: "/create",
        element: <CreatePost />,
      },
      {
        path: "/profile",
        element: <AboutMe />,
      },
      
    ],
  },
]);
