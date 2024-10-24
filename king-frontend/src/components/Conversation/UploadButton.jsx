import {styled} from "@mui/joy"

const UploadButton = ({setShowConversation}) => {
    const VisuallyHiddenInput = styled('input')`
        clip: rect(0 0 0 0);
        clip-path: inset(50%);
        height: 1px;
        overflow: hidden;
        position: absolute;
        bottom: 0;
        left: 0;
        white-space: nowrap;
        width: 1px;
    `

    return (
        <h1>Hello, World!</h1>
    )
}

export default UploadButton