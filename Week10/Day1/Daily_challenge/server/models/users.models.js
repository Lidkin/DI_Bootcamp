const db = require('../config/db.js');

const _register = async ({ firstname, lastname, email, password }) => {
    const trx = await db.transaction();
    try {
        const user = await db('users')
            .insert({ firstname, lastname, email }, ['id', 'firstname', 'lastname', 'email'])
            .transacting(trx);
        const hashpwd = await db('hashpwd')
            .insert({ userid: user[0].id, password }, ['userid', 'password'])
            .transacting(trx);
        await trx.commit();
        return hashpwd;
    } catch (error) {
        console.log(error);
        trx.rollback();
    }
};

const _login = async ({ firstname, lastname, password }) => {
    try {
        const userId = await db('users')
            .select('id')
            .where({ firstname, lastname });
        const hash = await db('hashpwd')
            .select('password')
            .where({ userid: userId[0].id });
        return hash[0].password;
    } catch (error) {
        console.log(error);
    }
}


const _allUsers = async () => {
    try {
        const users = await db('users')
            .select('firstname', 'lastname', 'email');
        return users;
    } catch (error) {
        console.log(error);
    }
} 

const _getUser = async (id) => {
    try {
        const user = await db('users')
            .select('firstname', 'lastname', 'email')
            .where({ id });
        return user;
    } catch (error) {
        console.log(error);
    }
}

const _putUser = async ({ firstname, lastname, email }, id) => {
    try {
        const user = await db('users')
            .update({ firstname, lastname, email }, ['firstname', 'lastname', 'email'])
            .where({ id });
        return user;
    } catch (error) {
        console.log(error);
    }
}

module.exports = { _register, _login, _allUsers, _getUser, _putUser };