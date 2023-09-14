import React from "react";

class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = { error: null, errorInfo: null };
    }

    componentDidCatch(error, errorInfo) {
        console.log(error, errorInfo)
        this.setState({ error: error, errorInfo: errorInfo });
    }

    render() {
        if (this.state.error) {
            console.log(this.state.error)
            return (
                <>
                    <h2>Something went wrong.</h2>
                    <details style={{ whiteSpace: 'pre-wrap' }}>
                        {this.state.error && this.state.error.toString()}
                        <br />
                        {this.state.errorInfo.componentStack}
                    </details>
               </>
            )
        }
        console.log(this.props.children)
        return this.props.children;
    }
}

export default ErrorBoundary;