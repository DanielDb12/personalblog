import axios from "axios";

import {
  GET_BLOG_LIST_SUCCESS,
  GET_BLOG_LIST_FAIL,
  GET_BLOG_SUCCESS,
  GET_BLOG_FAIL,
  GET_BLOG_LIST_CATEGORIES_FAIL,
  GET_BLOG_LIST_CATEGORIES_SUCCESS,
  GET_SEARCH_BLOG_SUCCESS,
  GET_SEARCH_BLOG_FAIL,
} from "./types";

export const get_blog_list = () => async dispatch => {

  const config = {
    header: {
      'Accept': 'application/json'
    }
  };

  try {
    const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/blog/`, config);


  }

}
