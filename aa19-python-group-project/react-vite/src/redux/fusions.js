// Action Types
const FETCH_FUSIONS_START = 'fusions/fetchStart';
const FETCH_FUSIONS_SUCCESS = 'fusions/fetchSuccess';
const FETCH_FUSIONS_FAILURE = 'fusions/fetchFailure';

// Action Creators
const fetchFusionsStart = () => ({
  type: FETCH_FUSIONS_START,
});

const fetchFusionsSuccess = (fusions) => ({
  type: FETCH_FUSIONS_SUCCESS,
  payload: fusions,
});

const fetchFusionsFailure = (error) => ({
  type: FETCH_FUSIONS_FAILURE,
  payload: error,
});

// Thunk Action
export const fetchFusions = () => async (dispatch) => {
    dispatch(fetchFusionsStart());
    try {
        const response = await fetch('/api/alchemy/fusions');
        if (!response.ok) {
            throw new Error('Failed to fetch fusions');
        }
        const data = await response.json();

        dispatch(fetchFusionsSuccess(data.fusions|| []));
    } catch (error) {
        dispatch(fetchFusionsFailure(error.message));
    }
};


// Initial State
const initialState = {
  list: [],
  status: 'idle', // idle, loading, succeeded, failed
  error: null,
};

// Reducer
function fusionsReducer(state = initialState, action) {
  switch (action.type) {
    case FETCH_FUSIONS_START:
      return {
        ...state,
        status: 'loading',
        error: null,
      };
    case FETCH_FUSIONS_SUCCESS:
      return {
        ...state,
        status: 'succeeded',
        list: action.payload,
      };
    case FETCH_FUSIONS_FAILURE:
      return {
        ...state,
        status: 'failed',
        error: action.payload,
      };
    default:
      return state;
  }
}

export default fusionsReducer;
