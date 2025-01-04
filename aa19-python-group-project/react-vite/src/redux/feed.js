const FETCH_FEED_START = 'feed/fetchStart';
const FETCH_FEED_SUCCESS = 'feed/fetchSuccess';
const FETCH_FEED_FAILURE = 'feed/fetchFailure';

const fetchFeedStart = () => ({
  type: FETCH_FEED_START,
});

const fetchFeedSuccess = (feedData) => ({
  type: FETCH_FEED_SUCCESS,
  payload: feedData,
});

const fetchFeedFailure = (error) => ({
  type: FETCH_FEED_FAILURE,
  payload: error,
});


export const fetchFeed = () => async (dispatch) => {
  dispatch(fetchFeedStart());
  try {
    const response = await fetch('/api/content_sources/feed');
    if (!response.ok) {
      throw new Error('Failed to conjure your feed 🧙‍♀️. Try again soon!');
    }
    const data = await response.json();
    dispatch(fetchFeedSuccess(data.data.sources)); // Adjust based on backend response
  } catch (error) {
    dispatch(fetchFeedFailure(error.message));
  }
};


const initialState = {
  list: [],
  status: 'idle',
  error: null,
};

function feedReducer(state = initialState, action) {
  switch (action.type) {
    case FETCH_FEED_START:
      return { ...state, status: 'loading', error: null };
    case FETCH_FEED_SUCCESS:
      return { ...state, status: 'succeeded', list: action.payload };
    case FETCH_FEED_FAILURE:
      return { ...state, status: 'failed', error: action.payload };
    default:
      return state;
  }
}

export default feedReducer;
