const FETCH_FEED_START = "feed/fetchStart";
const FETCH_FEED_SUCCESS = "feed/fetchSuccess";
const FETCH_FEED_FAILURE = "feed/fetchFailure";

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

export const fetchFeed = ({ page = 1, each_page = 10 } = {}) => async (dispatch) => {
  dispatch(fetchFeedStart());
  try {
    const response = await fetch(
      `/api/content_sources/feed?page=${page}&each_page=${each_page}`,
      { credentials: "include" }
    );
    if (!response.ok) {
      throw new Error("Failed to conjure your feed 🧙‍♀️. Try again soon!");
    }
    const data = await response.json();
    console.log("Fetched Feed Data:", data);
    dispatch(fetchFeedSuccess(data.data) || []);
  } catch (error) {
    console.error("Feed Fetch Error:", error.message);
    dispatch(fetchFeedFailure(error.message));
  }
};

const initialState = {
  list: [],
  status: "idle",
  error: null,
  total_pages: 0,
};

function feedReducer(state = initialState, action) {
  switch (action.type) {
    case FETCH_FEED_SUCCESS:{
      console.log("Payload:", action.payload);

      return {
        ...state,
        status: "succeeded",
        list: action.payload.sources.flatMap((source) => source.posts || []), // Flatten posts from all sources
        total_pages: action.payload.total_pages || 0// Start with 0 as the default max
      };
    }
    default:
      return state;
  }
}

export default feedReducer;
