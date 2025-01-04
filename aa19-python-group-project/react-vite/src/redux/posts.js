// Action Types
const CREATE_POST = 'posts/CREATE_POST';
const CREATE_POST_ERROR = 'posts/CREATE_POST_ERROR';

// Action Creators
const createPost = (post) => ({
  type: CREATE_POST,
  payload: post,
});

const createPostError = (error) => ({
  type: CREATE_POST_ERROR,
  payload: error,
});

// Thunk Action Creator for creating a post
export const thunkCreatePost = (postData) => async (dispatch) => {
  try {
    const response = await fetch('/api/posts/', {
      method: 'POST',
      body: postData,
    });

    if (response.ok) {
      const post = await response.json();
      dispatch(createPost(post));
    } else {
      const error = await response.json();
      dispatch(createPostError(error));
    }
  } catch (err) {
    dispatch(createPostError({ message: 'Something went wrong. Please try again.' }));
  }
};

// Reducer
const initialState = {
  posts: [],
  error: null,
};

const postsReducer = (state = initialState, action) => {
  switch (action.type) {
    case CREATE_POST:
      return {
        ...state,
        posts: [...state.posts, action.payload],
        error: null,
      };
    case CREATE_POST_ERROR:
      return {
        ...state,
        error: action.payload,
      };
    default:
      return state;
  }
};

export default postsReducer;
