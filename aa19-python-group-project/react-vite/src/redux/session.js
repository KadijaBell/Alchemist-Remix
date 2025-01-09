const SET_USER = 'session/setUser';
const REMOVE_USER = 'session/removeUser';

const setUser = (user) => ({
  type: SET_USER,
  payload: user
});

const removeUser = () => ({
  type: REMOVE_USER
});
// export const thunkAuthenticate = () => async (dispatch) => {
// 	// const response = await fetch("/api/auth/");
// 	// if (response.ok) {
// 	// 	const data = await response.json();
// 	// 	if (data.errors) {
// 	// 		return;
// 	// 	}

// 	// 	dispatch(setUser(data));
// 	// }else{
//   //   return null;
//   // }
// //   const response = await fetch("/api/auth/", {
// //       method: "GET",
// //       headers: {
// //         "Content-Type": "application/json",
// //       },
// //       credentials: "include",
// //     });

// //     if (response.ok) {
// //       const data = await response.json();
// //       if (data.user) {
// //         dispatch(setUser(data.user));
// //         return data.user;
// //       } else {
// //         // If no user is logged in, clear Redux state
// //         dispatch(removeUser());
// //         return null;
// //       }
// //     } else {
// //       console.error("Unexpected error in authentication:", response);
// //       dispatch(removeUser());
// //       return null;
// //     }
// //  };
//   console.log("Checking authentication...");
//   const response = await fetch("/api/auth/", {
//     method: "GET",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     credentials: "include",
//   });

//   if (response.ok) {
//     const data = await response.json();
//     console.log("Authentication response data:", data);
//     if (data.user) {
//       dispatch(setUser(data.user));
//       return data.user;
//     } else {
//       dispatch(removeUser());
//       return null;
//     }
//   } else {
//     console.error("Unexpected error in authentication:", response);
//     dispatch(removeUser());
//     return null;
//   }
// };
export const thunkAuthenticate = () => async (dispatch) => {
  try {
    const response = await fetch("/api/auth/", {
      method: "GET",
      credentials: "include",
    });

    if (!response.ok) {
      console.error("Failed to authenticate:", response.statusText);
      dispatch(removeUser());
      return null;
    }

    const data = await response.json();
    console.log("Authentication response:", data);

    if (data.user) {
      dispatch(setUser(data.user));
       return data.user;
    } else {
      dispatch(removeUser());
      return null;
    }
  } catch (error) {
    console.error("Error during authentication:", error);
    dispatch(removeUser());
    return null;
  }
};




export const thunkLogin = (credentials) => async (dispatch) => {
  const response = await fetch("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(credentials),
  });

  if (response.ok) {
      const data = await response.json();
      dispatch(setUser(data));
      return true;
  } else if (response.status < 500) {
      const errorMessages = await response.json();
      return { errors: errorMessages.errors };
  } else {
      return { errors: { server: "Something went wrong. Please try again." } };
  }
};


export const thunkSignup = (user) => async (dispatch) => {
  const response = await fetch("/api/auth/signup", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(user)
  });

  if(response.ok) {
    const data = await response.json();
    dispatch(setUser(data));
    return true;
  } else if (response.status < 500) {
    const errorMessages = await response.json();
    return { errors: errorMessages }
  } else {
    return { server: "Something went wrong. Please try again" }
  }
};

export const thunkLogout = () => async (dispatch) => {
  await fetch("/api/auth/logout");
  dispatch(removeUser());
};

export const thunkRestoreUser = () => async (dispatch) => {
  try {
  const response = await fetch("/api/auth/restore", {
    method: "GET",
    credentials: "include",
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(setUser(data));
    return data;
  } else {
    dispatch(removeUser());
    return false;
    }
  } catch (error) {
      console.error("Error restoring user session:", error);
      dispatch(removeUser());
  }
  };
const initialState = { user: null };

function sessionReducer(state = initialState, action) {
  switch (action.type) {
    case SET_USER:
      return { ...state, user: action.payload };
    case REMOVE_USER:
      return { ...state, user: null };
    default:
      return state;
  }
}

export default sessionReducer;
