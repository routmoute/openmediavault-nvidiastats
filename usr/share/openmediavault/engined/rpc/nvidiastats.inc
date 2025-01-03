<?php

class OMVRpcServiceNvidiaStats extends \OMV\Rpc\ServiceAbstract
{
    public function getName()
    {
        return "NvidiaStats";
    }

    public function initialize()
    {
        $this->registerMethod("gputemp");
        $this->registerMethod("gpuutil");
    }

    public function gputemp($param, $context)
    {
        // Validate the RPC caller context.
        $this->validateMethodContext($context, ["role" => OMV_ROLE_EVERYONE]);
        // get cpu temp command and divisor number
        $gpuTemp = \OMV\Environment::get("OMV_NVIDIA_GPU_TEMP_COMMAND",
          "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader");
        $cmd = new \OMV\System\Process($gpuTemp);
        $cmd->execute($output, $exitStatus);
        return [
            "gputemp" => intval($output[0])
        ];
    }

    public function gpuutil($param, $context)
    {
        // Validate the RPC caller context.
        $this->validateMethodContext($context, ["role" => OMV_ROLE_EVERYONE]);
        // get cpu temp command and divisor number
        $gpuUtil = \OMV\Environment::get("OMV_NVIDIA_GPU_UTIL_COMMAND",
          "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader");
        $cmd = new \OMV\System\Process($gpuUtil);
        $cmd->execute($output, $exitStatus);
        return [
            "gpuutil" => intval($output[0])
        ];
    }
}
