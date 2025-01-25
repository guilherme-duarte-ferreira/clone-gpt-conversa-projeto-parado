export const TypingIndicator = () => {
  return (
    <div className="flex items-center space-x-2 px-4 py-3 rounded-lg bg-chat-assistant border border-gray-200 max-w-[85%] mb-4">
      <div className="flex space-x-1">
        <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:-0.3s]" />
        <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:-0.15s]" />
        <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" />
      </div>
    </div>
  );
};