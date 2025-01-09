// // Action Types
// const FETCH_POSTS_START = "posts/fetchStart";
// const FETCH_POSTS_SUCCESS = "posts/fetchSuccess";
// const FETCH_POSTS_FAILURE = "posts/fetchFailure";
// const CREATE_POST_SUCCESS = "posts/createSuccess";
// const CREATE_POST_FAILURE = "posts/createFailure";
// const UPDATE_POST_SUCCESS = "posts/updateSuccess";
// const UPDATE_POST_FAILURE = "posts/updateFailure";
// const DELETE_POST_SUCCESS = "posts/deleteSuccess";
// const DELETE_POST_FAILURE = "posts/deleteFailure";

// // Action Creators
// const fetchPostsStart = () => ({
//   type: FETCH_POSTS_START,
// });

// const fetchPostsSuccess = (posts) => ({
//   type: FETCH_POSTS_SUCCESS,
//   payload: posts,
// });

// const fetchPostsFailure = (error) => ({
//   type: FETCH_POSTS_FAILURE,
//   payload: error,
// });

// const createPostSuccess = (post) => ({
//   type: CREATE_POST_SUCCESS,
//   payload: post,
// });

// const createPostFailure = (error) => ({
//   type: CREATE_POST_FAILURE,
//   payload: error,
// });

// const updatePostSuccess = (post) => ({
//   type: UPDATE_POST_SUCCESS,
//   payload: post,
// });

// const updatePostFailure = (error) => ({
//   type: UPDATE_POST_FAILURE,
//   payload: error,
// });

// const deletePostSuccess = (postId) => ({
//   type: DELETE_POST_SUCCESS,
//   payload: postId,
// });

// const deletePostFailure = (error) => ({
//   type: DELETE_POST_FAILURE,
//   payload: error,
// });

// // Thunks
// export const fetchPosts = (page = 1, perPage = 10) => async (dispatch, getState) => {
//   dispatch(fetchPostsStart());
//   const { token } = getState().session; // Assuming you have a session slice with a token
//   try {
//     const response = await fetch(`/api/posts?page=${page}&per_page=${perPage}`, {
//       headers: {
//         Authorization: `Bearer ${token}`,
//       },
//     });
//     if (!response.ok) {
//       throw new Error("Failed to fetch posts");
//     }
//     const data = await response.json();
//     dispatch(fetchPostsSuccess(data));
//   } catch (error) {
//     dispatch(fetchPostsFailure(error.message));
//   }
// };

// export const thunkCreatePost = (formData) => async (dispatch, getState) => {
//   const { token } = getState().session; // Assuming you have a session slice with a token
//   try {
//     const response = await fetch("/api/posts", {
//       method: "POST",
//       headers: {
//         Authorization: `Bearer ${token}`,
//       },
//       body: formData,
//     });
//     if (!response.ok) {
//       throw new Error("Failed to create post");
//     }
//     const post = await response.json();
//     dispatch(createPostSuccess(post));
//     dispatch(fetchPosts());
//   } catch (error) {
//     dispatch(createPostFailure(error.message));
//   }
// };

// export const thunkUpdatePost = (postId, formData) => async (dispatch, getState) => {
//   const { token } = getState().session; // Assuming you have a session slice with a token
//   try {
//     const response = await fetch(`/api/posts/${postId}`, {
//       method: "PUT",
//       headers: {
//         Authorization: `Bearer ${token}`,
//       },
//       body: formData,
//     });
//     if (!response.ok) {
//       throw new Error("Failed to update post");
//     }
//     const post = await response.json();
//     dispatch(updatePostSuccess(post));
//     dispatch(fetchPosts());
//   } catch (error) {
//     dispatch(updatePostFailure(error.message));
//   }
// };

// export const thunkDeletePost = (postId) => async (dispatch, getState) => {
//   const { token } = getState().session; // Assuming you have a session slice with a token
//   try {
//     const response = await fetch(`/api/posts/${postId}`, {
//       method: "DELETE",
//       headers: {
//         Authorization: `Bearer ${token}`,
//       },
//     });
//     if (!response.ok) {
//       throw new Error("Failed to delete post");
//     }
//     await response.json();
//     dispatch(deletePostSuccess(postId));
//     dispatch(fetchPosts());
//   } catch (error) {
//     dispatch(deletePostFailure(error.message));
//   }
// };

// // Initial State
// const initialState = {
//   list: [],
//   status: "idle",
//   error: null,
//   page: 1,
//   total_pages: 1,
// };

// // Reducer
// const postsReducer = (state = initialState, action) => {
//   switch (action.type) {
//     case FETCH_POSTS_START:
//       return {
//         ...state,
//         status: "loading",
//       };
//     case FETCH_POSTS_SUCCESS:
//       return {
//         ...state,
//         list: action.payload.posts,
//         status: "succeeded",
//         page: action.payload.page,
//         total_pages: action.payload.total_pages,
//       };
//     case FETCH_POSTS_FAILURE:
//       return {
//         ...state,
//         status: "failed",
//         error: action.payload,
//       };
//     case CREATE_POST_SUCCESS:
//       return {
//         ...state,
//         list: [...state.list, action.payload],
//         error: null,
//       };
//     case CREATE_POST_FAILURE:
//       return {
//         ...state,
//         error: action.payload,
//       };
//     case UPDATE_POST_SUCCESS:
//       return {
//         ...state,
//         list: state.list.map((post) =>
//           post.id === action.payload.id ? action.payload : post
//         ),
//         error: null,
//       };
//     case UPDATE_POST_FAILURE:
//       return {
//         ...state,
//         error: action.payload,
//       };
//     case DELETE_POST_SUCCESS:
//       return {
//         ...state,
//         list: state.list.filter((post) => post.id !== action.payload),
//         error: null,
//       };
//     case DELETE_POST_FAILURE:
//       return {
//         ...state,
//         error: action.payload,
//       };
//     default:
//       return state;
//   }
// };

// export default postsReducer;



// // Action Types
// const FETCH_POSTS_START = "posts/fetchStart";
// const FETCH_POSTS_SUCCESS = "posts/fetchSuccess";
// const FETCH_POSTS_FAILURE = "posts/fetchFailure";
// const CREATE_POST_SUCCESS = "posts/createSuccess";
// const CREATE_POST_FAILURE = "posts/createFailure";
// const UPDATE_POST_SUCCESS = "posts/updateSuccess";
// const UPDATE_POST_FAILURE = "posts/updateFailure";
// const DELETE_POST_SUCCESS = "posts/deleteSuccess";
// const DELETE_POST_FAILURE = "posts/deleteFailure";

// // Action Creators
// const fetchPostsStart = () => ({
//   type: FETCH_POSTS_START,
// });

// const fetchPostsSuccess = (posts) => ({
//   type: FETCH_POSTS_SUCCESS,
//   payload: posts,
// });

// const fetchPostsFailure = (error) => ({
//   type: FETCH_POSTS_FAILURE,
//   payload: error,
// });

// const createPostSuccess = (post) => ({
//   type: CREATE_POST_SUCCESS,
//   payload: post,
// });

// const createPostFailure = (error) => ({
//   type: CREATE_POST_FAILURE,
//   payload: error,
// });

// const updatePostSuccess = (post) => ({
//   type: UPDATE_POST_SUCCESS,
//   payload: post,
// });

// const updatePostFailure = (error) => ({
//   type: UPDATE_POST_FAILURE,
//   payload: error,
// });

// const deletePostSuccess = (postId) => ({
//   type: DELETE_POST_SUCCESS,
//   payload: postId,
// });

// const deletePostFailure = (error) => ({
//   type: DELETE_POST_FAILURE,
//   payload: error,
// });

// // Thunks
// export const fetchPosts = (page = 1, perPage = 10) => async (dispatch, getState) => {
//   dispatch(fetchPostsStart());
//   const { token } = getState().session; // Assuming you have a session slice with a token
//   try {
//     const response = await fetch(`/api/posts?page=${page}&per_page=${perPage}`, {
//       headers: {
//         Authorization: `Bearer ${token}`,
//       },
//     });
//     if (!response.ok) {
//       throw new Error("Failed to fetch posts");
//     }
//     const data = await response.json();
//     dispatch(fetchPostsSuccess(data));
//   } catch (error) {
//     dispatch(fetchPostsFailure(error.message));
//   }
// };

// export const thunkCreatePost = (formData) => async (dispatch, getState) => {
//   const { token } = getState().session; // Assuming you have a session slice with a token
//   try {
//     const response = await fetch("/api/posts", {
//       method: "POST",
//       headers: {
//         Authorization: `Bearer ${token}`,
//       },
//       body: formData,
//     });
//     if (!response.ok) {
//       throw new Error("Failed to create post");
//     }
//     const post = await response.json();
//     dispatch(createPostSuccess(post));
//     dispatch(fetchPosts());
//     return post;
//   } catch (error) {
//     dispatch(createPostFailure(error.message));
//     return { errors: error.message };
//   }
// };

// export const thunkUpdatePost = (postId, formData) => async (dispatch, getState) => {
//   const { token } = getState().session; // Assuming you have a session slice with a token
//   try {
//     const response = await fetch(`/api/posts/${postId}`, {
//       method: "PUT",
//       headers: {
//         Authorization: `Bearer ${token}`,
//       },
//       body: formData,
//     });
//     if (!response.ok) {
//       throw new Error("Failed to update post");
//     }
//     const post = await response.json();
//     dispatch(updatePostSuccess(post));
//     dispatch(fetchPosts());
//   } catch (error) {
//     dispatch(updatePostFailure(error.message));
//   }
// };

// export const thunkDeletePost = (postId) => async (dispatch, getState) => {
//   const { token } = getState().session; // Assuming you have a session slice with a token
//   try {
//     const response = await fetch(`/api/posts/${postId}`, {
//       method: "DELETE",
//       headers: {
//         Authorization: `Bearer ${token}`,
//       },
//     });
//     if (!response.ok) {
//       throw new Error("Failed to delete post");
//     }
//     await response.json();
//     dispatch(deletePostSuccess(postId));
//     dispatch(fetchPosts());
//   } catch (error) {
//     dispatch(deletePostFailure(error.message));
//   }
// };

// // Initial State
// const initialState = {
//   list: [],
//   status: "idle",
//   error: null,
//   page: 1,
//   total_pages: 1,
// };

// // Reducer
// const postsReducer = (state = initialState, action) => {
//   switch (action.type) {
//     case FETCH_POSTS_START:
//       return {
//         ...state,
//         status: "loading",
//       };
//     case FETCH_POSTS_SUCCESS:
//       return {
//         ...state,
//         list: action.payload.posts,
//         status: "succeeded",
//         page: action.payload.page,
//         total_pages: action.payload.total_pages,
//       };
//     case FETCH_POSTS_FAILURE:
//       return {
//         ...state,
//         status: "failed",
//         error: action.payload,
//       };
//     case CREATE_POST_SUCCESS:
//       return {
//         ...state,
//         list: [...state.list, action.payload],
//         error: null,
//       };
//     case CREATE_POST_FAILURE:
//       return {
//         ...state,
//         error: action.payload,
//       };
//     case UPDATE_POST_SUCCESS:
//       return {
//         ...state,
//         list: state.list.map((post) =>
//           post.id === action.payload.id ? action.payload : post
//         ),
//         error: null,
//       };
//     case UPDATE_POST_FAILURE:
//       return {
//         ...state,
//         error: action.payload,
//       };
//     case DELETE_POST_SUCCESS:
//       return {
//         ...state,
//         list: state.list.filter((post) => post.id !== action.payload),
//         error: null,
//       };
//     case DELETE_POST_FAILURE:
//       return {
//         ...state,
//         error: action.payload,
//       };
//     default:
//       return state;
//   }
// };

// export default postsReducer;

const FETCH_POSTS_START = "posts/fetchStart";
const FETCH_POSTS_SUCCESS = "posts/fetchSuccess";
const FETCH_POSTS_FAILURE = "posts/fetchFailure";

const initialState = {
  list: [],
  status: "idle",
  error: null,
  page: 1,
  total_pages: 1,

};

export const thunkCreatePost = (formData) => async (dispatch) => {
  try {
    const response = await fetch("/api/posts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });

    if (!response.ok) {
      throw new Error("Failed to create post");
    }

    const newPost = await response.json();
    dispatch({ type: "CREATE_POST_SUCCESS", payload: newPost });
  } catch (error) {
    dispatch({ type: "CREATE_POST_FAILURE", payload: error.message });
  }
};


export const fetchPosts = (page = 1, perPage = 10) => async (dispatch) => {
  dispatch({ type: "posts/fetchStart" });
  try {
    const response = await fetch(`/api/posts?page=${page}&per_page=${perPage}`);
    if (!response.ok) {
      throw new Error("Failed to fetch posts");
    }
    const data = await response.json();
    dispatch({ type: "posts/fetchSuccess", payload: data });
  } catch (error) {
    dispatch({ type: "posts/fetchFailure", payload: error.message });
  }
};

const postsReducer = (state = initialState, action) => {
  console.log("Action received:", action); // Debugging log
  switch (action.type) {
    case FETCH_POSTS_START:
      return {
        ...state,
        status: "loading",
        error: null,
      };
    case FETCH_POSTS_SUCCESS:
      return {
        ...state,
        list: action.payload.posts,
        page: action.payload.page,
        total_pages: action.payload.total_pages,
        status: "succeeded",
      };
    case FETCH_POSTS_FAILURE:
      return {
        ...state,
        status: "failed",
        error: action.payload,
      };
    default:
      return state;
  }
};

export default postsReducer;
