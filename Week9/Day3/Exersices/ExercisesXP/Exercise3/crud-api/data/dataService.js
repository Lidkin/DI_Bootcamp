const axios = require("axios");

const fetchPosts = async (url) => {
    try {
        const response = await axios.get(url);
        return response.data;
    } catch (error) {
        console.error('Error fetching posts:', error);
        throw error;
    }
}

module.exports = fetchPosts;