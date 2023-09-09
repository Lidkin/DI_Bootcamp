const fillPost = () => { 
    let posts = [];
    for (let i = 1; i < 11; i++) {
        posts.push({ id: i, title: `title${i}`, content: `content${i}` });
    };
    return posts;
}

const postsDB = fillPost();
const posts = [...postsDB];

module.exports = { posts };