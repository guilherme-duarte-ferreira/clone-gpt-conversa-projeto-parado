import { cn } from "@/lib/utils";

interface ChatMessageProps {
  content: string;
  role: "user" | "assistant";
}

export const ChatMessage = ({ content, role }: ChatMessageProps) => {
  return (
    <div
      className={cn(
        "px-4 py-3 rounded-lg max-w-[85%] mb-4",
        role === "user"
          ? "bg-chat-user ml-auto"
          : "bg-chat-assistant border border-gray-200"
      )}
    >
      <p className="text-gray-800 text-sm md:text-base">{content}</p>
    </div>
  );
};